import json
import subprocess
import sys
import serial
import time

CONFIG_PATH = "/home/jakub/Documents/projekt/AdaptBoard-keypad/serial_app/config.json"

# Throttle analog events to avoid flooding expensive actions (pactl/osd).
ANALOG_MIN_INTERVAL = 0.02
ANALOG_MIN_DELTA = 0

# Warning thresholds for always-on listener
WARN_RATE_WINDOW = 1.0
WARN_MSG_RATE = 80  # messages per second
WARN_NOISY_ANALOG = 30  # noisy analog events per second per channel
WARN_COOLDOWN = 10.0  # seconds

def notify_warning(title, message, warn_state):
    now = time.monotonic()
    last = warn_state.get("last_warn", 0.0)
    if (now - last) < WARN_COOLDOWN:
        return
    warn_state["last_warn"] = now
    try:
        subprocess.Popen(["notify-send", title, message])
    except Exception:
        pass

def load_config():
    with open(CONFIG_PATH, "r", encoding="utf-8") as f:
        return json.load(f)

def run_action(action, value=None):
    shell_cmd = action.get("shell")
    if not shell_cmd:
        return
    if action.get("pass_value") and value is not None:
        suffix = action.get("suffix", "")
        shell_cmd = f"{shell_cmd} {value}{suffix}"
    subprocess.Popen(shell_cmd, shell=True)

def handle_event(evt, actions, analog_state=None, warn_state=None):
    evt_type = evt.get("type")
    evt_id = str(evt.get("id"))

    if evt_type == "key":
        action = actions.get("key", {}).get(evt_id)
        if not action:
            return
        required_state = action.get("state")
        if required_state and evt.get("state") != required_state:
            return
        run_action(action)

    elif evt_type == "analog":
        action = actions.get("analog", {}).get(evt_id)
        if not action:
            return
        value = evt.get("value")
        if value is None:
            return
        try:
            value = float(value)
        except (TypeError, ValueError):
            return
        factor = action.get("factor")
        if factor is not None:
            try:
                value = value * float(factor)
            except (TypeError, ValueError):
                return
        if isinstance(value, float) and value.is_integer():
            value = int(value)
        if analog_state is not None:
            state = analog_state.setdefault(evt_id, {"last_time": 0.0, "last_value": None})
            now = time.monotonic()
            last_value = state["last_value"]
            if last_value is not None:
                if abs(value - last_value) < ANALOG_MIN_DELTA and (now - state["last_time"]) < ANALOG_MIN_INTERVAL:
                    return
            state["last_time"] = now
            state["last_value"] = value
            if warn_state is not None:
                noisy = warn_state.setdefault("noisy", {})
                bucket = noisy.setdefault(evt_id, {"start": now, "count": 0})
                if (now - bucket["start"]) > WARN_RATE_WINDOW:
                    bucket["start"] = now
                    bucket["count"] = 0
                bucket["count"] += 1
                if bucket["count"] > WARN_NOISY_ANALOG:
                    notify_warning(
                        "Serial listener warning",
                        f"Noisy analog channel {evt_id}: {bucket['count']}/s",
                        warn_state,
                    )
        run_action(action, value=value)

def main():
    cfg = load_config()
    serial_cfg = cfg.get("serial", {})
    actions = cfg.get("actions", {})

    port = serial_cfg.get("port", "/dev/ttyACM0")
    baud = serial_cfg.get("baud", 115200)
    timeout = serial_cfg.get("timeout", 1)

    analog_state = {}
    warn_state = {"last_warn": 0.0, "rate": {"start": time.monotonic(), "count": 0}, "noisy": {}}

    with serial.Serial(port, baud, timeout=timeout) as ser:
        while True:
            line = ser.readline()
            if not line:
                continue
            try:
                text = line.decode("utf-8", errors="replace").strip()
                evt = json.loads(text)
            except Exception:
                continue
            rate = warn_state.get("rate")
            now = time.monotonic()
            if (now - rate["start"]) > WARN_RATE_WINDOW:
                rate["start"] = now
                rate["count"] = 0
            rate["count"] += 1
            if rate["count"] > WARN_MSG_RATE:
                notify_warning(
                    "Serial listener warning",
                    f"High serial message rate: {rate['count']}/s",
                    warn_state,
                )
            handle_event(evt, actions, analog_state, warn_state)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        pass