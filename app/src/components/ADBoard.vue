<template>
  <div>
    <div class="AD-Board">
      <div
        class="AD-Key"
        v-for="(key, index) in keys"
        :key="'Key' + key.id"
      >
        <input
          type="radio"
          name="radio"
          :id="'radio-' + index"
          :value="index"
          v-model="selectedKey"
        />
        <label :for="'radio-' + index">
          <p>Key {{ key.id }}</p>
          <!-- select shuffle/switch -->
          <select
            name="select"
            v-model="keys[index]['type']"
          >
            <option value="switch">Switch</option>
            <option value="shuffle" v-if="keys[index].id > 11">Shuffle</option>
            <option value="text">Text</option>
            <option value="pot" v-if="keys[index].id > 3">Potmeter</option>
            <option value="display">Display</option>
          </select>

          <!-- shortcut display -->
          <div
            class="short-cut-on-key"
            v-if="keys[index]['type'] === 'switch'"
          >
            <div v-for="(item, i) in keys[index]['shortCut']" :key="i">
              <p>{{ item }}</p>
              <p v-if="i < keys[index]['shortCut'].length - 1">+</p>
            </div>
          </div>

          <!-- text box -->
          <div v-else-if="keys[index]['type'] === 'text'">
            <input
              v-model="keys[index]['text']"
              @keypress="blockString($event)"
              type="text"
              name="text"
              onpaste="return false;"
              autocomplete="off"
            />
          </div>

          <!-- shuffle action select -->
          <div class="shuffle-cl" v-if="keys[index]['type'] === 'shuffle' || keys[index]['type'] === 'pot'">
            <select
              name="shuffleSelect"
              v-model="keys[index]['shuffleAction']"
            >
              <option :value="['VOLUME_INCREMENT', 'VOLUME_DECREMENT']">
                Volume control
              </option>
              <option
                :value="['BRIGHTNESS_INCREMENT','BRIGHTNESS_DECREMENT']"
              >
                Brightness control
              </option>
            </select>
            <div>
              <button @click="shuffleDirChange(index)">
                <p v-if="keys[index]['shuffleDir'] === 'down'">↓</p>
                <p v-if="keys[index]['shuffleDir'] === 'up'">↑</p>
              </button>
              <!-- work in progress here ↓ -->
              <input
                @keypress="blockNumber($event)"
                type="number"
                name="steps"
                min="0"
                max="100"
                onpaste="return false;"
                v-model="keys[index]['steps']"
              />
            </div>
          </div>
        </label>
      </div>
    </div>
    <button @click="saveFile()">Save</button>
  </div>
</template>

<script>
export default {
  props: {
    shortCut: Array
  },
  name: 'ADBoard',
  methods: {
    shuffleDirChange(index) {
      if (this.keys[index]['shuffleDir'] === 'down') {
        this.keys[index]['shuffleDir'] = 'up';
      } else if (this.keys[index]['shuffleDir'] === 'up') {
        this.keys[index]['shuffleDir'] = 'down';
      }
    },
    saveFile() {
      let stringFile = 'from adafruit_hid.consumer_control_code import ConsumerControlCode # type: ignore\nfrom adafruit_hid.keycode import Keycode # type: ignore\nfrom micropython import const # type: ignore\n\n';
      // create MATRIX_ACTIONS
      stringFile += 'MATRIX_ACTIONS = {\n';
      for (let i = 0; i < this.keys.length; i++) {
        // if it is shortcut
        if (this.keys[i].type === "switch" || this.keys[i].type === "text" && this.keys[i].ccCode == false) {
          if (this.keys[i].type === "switch" && this.keys[i].ccCode == false) {
            stringFile += '    ' + this.keys[i].id + ': lambda cc, kdb, layout: kdb.send(';
            for (let j = 0; j < this.keys[i].shortCut.length; j++) {
              const element = this.keys[i].shortCut[j];
              stringFile += 'Keycode.' + element;
              if (j != this.keys[i].shortCut.length - 1) {
                stringFile += ', ';
              }
            }
            stringFile += '),\n';
          } else if (this.keys[i].type === "text" && this.keys[i].ccCode == false) {
            stringFile += '    ' + this.keys[i].id + ': lambda cc, kdb, layout:   .write("' + this.keys[i].text + '"),\n';
          }
        }
      }
      stringFile += '}\n\n';

      // create ANALOG_ACTIONS
      stringFile += 'ANALOG_ACTIONS = {\n';
      for (let i = 0; i < this.keys.length; i++) {
        if (this.keys[i].type === "shuffle" || this.keys[i].type === "pot") {
          stringFile += '    ' + (Number(this.keys[i].id) - 4) + ': {\n';
          stringFile += '        ' + 'True: lambda cc, mouse: cc.send(ConsumerControlCode.' + (this.keys[i].shuffleDir === 'up' ? String(this.keys[i].shuffleAction[0]) : String(this.keys[i].shuffleAction[1])) + '),\n';
          stringFile += '        ' + 'False: lambda cc, mouse: cc.send(ConsumerControlCode.' + (this.keys[i].shuffleDir === 'up' ? String(this.keys[i].shuffleAction[1]) : String(this.keys[i].shuffleAction[0])) + '),\n';
          stringFile += '        ' + `"steps": ${this.keys[i].steps},\n`;
          stringFile += '        ' + '"type": "' + this.keys[i].type + '",\n';
          stringFile += '    },\n';
        }
      }
      stringFile += '}\n\n';

      // display turn on
      stringFile += 'DISPLAY_CONFIG = {\n    "present": const(';
      for (let i = 0; i < this.keys.length; i++) {
        if (this.keys[i].type === "display") {
          stringFile += 'True';
          break;
        } else if (i === this.keys.length - 1){
          stringFile += 'False';
        }
      }
      stringFile += '),\n    "WIDTH": const(128),\n    "HEIGHT": const(32),\n}';
      stringFile += '\n\nANALOG_THRESHOLD = const(100)';

      const blob = new Blob([stringFile], { type: "text/plain" });
      const link = document.createElement("a");
      link.download = "config.py";
      link.href = window.URL.createObjectURL(blob);
      link.click();
      link.remove();
    },
    capitalizeFirstLetter(string) {
      return string.charAt(0).toUpperCase() + string.slice(1);
    }, 
    blockString(event) {
      if (event.key === '"') {
        event.preventDefault();
      }
    },
    blockNumber(event) {
      if (['+', '-', '.'].includes(event.key)) {
        event.preventDefault();
      }
      if (event.key === '0' && event.target.value === '') {
        event.preventDefault();
      }
    },
    try() {
      let keys = [];
      let f = 20;
      for (let i = 0; i < 5; i++) {
        f -= 4;
        for (let k = 0; k < 4; k++) {
          keys.push({
          id: f,
          type: "switch",
          shortCut: ['LEFT_CONTROL', 'C'],
          ccCode: false,
          shuffleAction: ['VOLUME_INCREMENT', 'VOLUME_DECREMENT'],
          text: "",
          shuffleDir: "up",
          steps: 18,
          display: false,
        });
        f++;
        }
        f -= 4;
      };
      this.keys = keys;
    }
  },
  watch: {
    shortCut: function (newVal) {
      for (let i = 0; i < newVal.length; i++) {
        this.keys[this.selectedKey]['shortCut'] = newVal;        
      }
    },
  },
  mounted() {
    this.try();
  },
  data() {
    return {
      keys: [],
      selectedKey: 0,
    }
  },
}
</script>

<style lang="scss" scoped>
$color-palette: (
  "app": #f5f5f5,
  "button": #fff,
  "select": #f5f5f5,
  "hover": #d4d4d4,
  "checked": #b1b1b1,
  "text-border": #5c5c5c91,
);
$font-size-palette: (
  "h1-Title": 2rem,
  "AD-Name": 0.9rem,
  "switcher-s": 0.7rem,
  "ShortCut-s": 0.6rem,
  "SC-Board-s": 0.7rem,
);
$gap-size: 10px;
$gap-size-s: 3px;
$font-size: 1rem;
$border-radius: 5px;
  .AD-Board {
    display: grid;
    grid-template-columns: repeat(4, 1fr);
    grid-template-rows: repeat(5, 1fr);
    gap: $gap-size;

    .AD-Key {
        display: inherit;
      > label {
        background-color: map-get($map: $color-palette, $key: "button");
        border-radius: $border-radius;
        display: flex;
        flex-direction: column;
        gap: $gap-size;
        justify-content: space-around;
        align-items: center;
        transition: all 0.3s ease-in-out;
        padding: 10px;
        min-width: 130px;
        min-height: 100px;

        &:hover {
            background-color: map-get($map: $color-palette, $key: "hover");
        }
        > p:first-child {
          font-size: map-get($map: $font-size-palette, $key: "AD-Name");
        }
        select {
          font-size: map-get($map: $font-size-palette, $key: "switcher-s");
        }
        .short-cut-on-key {
          font-size: map-get($map: $font-size-palette, $key: "ShortCut-s");
          font-weight: bold;
          width: 80%;
          display: flex;
          gap: 5px;
          flex-wrap: wrap;
          justify-content: center;

          & > div {
            display: flex;
            gap: 5px;
          }
        }

        .shuffle-cl {
          display: flex;
          flex-direction: column;
          gap: 5px;
          justify-content: center;
          align-items: center;
          width: 100%;

          > div {
            gap: 5px;
            display: flex;
            button {
              padding: 4px 5px;
              background-color: map-get($map: $color-palette, $key: "app");
              outline: 1px solid rgba(0, 0, 0, 0.341);
              &:hover {
                background-color: #8d8d8d;
                color: black;
              }
            }
          }
          > label {
            display: flex;
            gap: 5px;
            align-items: center;
          }
          input[type="number"] {
            border: 1px solid map-get($map: $color-palette, $key: "text-border");
            border-radius: $border-radius;
          }
        }
      }
      input[type="text"] {
        width: 120px;
        border-radius: $border-radius;
        border: 1px solid map-get($map: $color-palette, $key: "text-border");
      }
      input[type="radio"]:checked + label {
        background-color: map-get($map: $color-palette, $key: "checked");
      }
      > input {
        display: none;
      }
      .only-switch {
        padding: 0px;
        margin: 0px;
      }
    }
  }
  select {
  background-color: map-get($map: $color-palette, $key: "select");
  border: none;
  width: auto;
  font-size: 1rem;
  font-weight: 500;
  border-radius: $border-radius;
  padding: 3px 10px 3px 3px;
  outline: 1px solid #d4d4d4;
  cursor: pointer;
  &:active,
  &:focus {
    outline: none;
    box-shadow: none;
  }
  & > option {
    padding: 5px;
  }
}
button {
  border: none;
  border-radius: $border-radius;
  padding: 10px;
  font-size: $font-size;
  cursor: pointer;
  background-color: #d4d4d4;
  transition: all 0.3s ease-in-out;

  &:hover {
    background-color: #8d8d8d;
    color: white;
  }

  p {
    margin: 0px;
  }
}
</style>