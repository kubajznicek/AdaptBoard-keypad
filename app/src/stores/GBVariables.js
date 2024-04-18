import { ref } from 'vue';
import { defineStore } from "pinia";

export const useGBVar = defineStore('Variables', () => {
    const fn = [
        { action: 'BRIGHTNESS_INCREMENT', info: 'Brightness Up' },
        { action: 'BRIGHTNESS_DECREMENT', info: 'Brightness Down' },
        { action: 'EJECT', info: 'Eject' },
        { action: 'FAST_FORWARD', info: 'fast forward' },
        { action: 'MUTE', info: 'Mute' },
        { action: 'PLAY_PAUSE', info: 'Play/Pause' },
        { action: 'RECORD', info: 'Record' },
        { action: 'REWIND', info: 'Rewind' },
        { action: 'SCAN_NEXT_TRACK', info: 'Next track' },
        { action: 'SCAN_PREVIOUS_TRACK', info: 'Previous track' },
        { action: 'STOP', info: 'Stop' },
        { action: 'VOLUME_DECREMENT', info: 'Volume Down' },
        { action: 'VOLUME_INCREMENT', info: 'Volume Up' },
    ]

    let keys = [];
    let f = 20;
    for (let i = 0; i < 5; i++) {
        f -= 4;
        for (let k = 0; k < 4; k++) {
            keys.push({
                id: f,
                type: "switch",
                shortCut: [{ value: 'LEFT_CONTROL', text: 'Ctrl' }, { value: 'C', text: 'C' }],
                ccCode: false,
                shuffleAction: ['VOLUME_INCREMENT', 'VOLUME_DECREMENT'],
                text: "",
                potDir: "up",
                steps: 18,
                display: false,
                info: 'Ctrl + C',
                action: 'short cut',
                fn: fn[0],
            });
            f++;
        };
        f -= 4;
    };

    const ADKeys = ref(keys)
    const ActiveKey = ref(0);
    const SCKeys = ref([
        [

            [
                { checked: false, value: 'ESCAPE', text: 'Esc', size: 1 },
                { value: 1, text: 'gap', size: 1 },
                { checked: false, value: 'F1', text: 'F1', size: 1 },
                { checked: false, value: 'F2', text: 'F2', size: 1 },
                { checked: false, value: 'F3', text: 'F3', size: 1 },
                { checked: false, value: 'F4', text: 'F4', size: 1 },
                { checked: false, value: 'F5', text: 'F5', size: 1 },
                { checked: false, value: 'F6', text: 'F6', size: 1 },
                { checked: false, value: 'F7', text: 'F7', size: 1 },
                { checked: false, value: 'F8', text: 'F8', size: 1 },
                { checked: false, value: 'F9', text: 'F9', size: 1 },
                { checked: false, value: 'F10', text: 'F10', size: 1 },
                { checked: false, value: 'F11', text: 'F11', size: 1 },
                { checked: false, value: 'F12', text: 'F12', size: 1 },
            ],
            [
                { checked: false, value: 'GRAVE_ACCENT', text: '`', size: 1 },
                { checked: false, value: 'ONE', text: '1', size: 1 },
                { checked: false, value: 'TWO', text: '2', size: 1 },
                { checked: false, value: 'THREE', text: '3', size: 1 },
                { checked: false, value: 'FOUR', text: '4', size: 1 },
                { checked: false, value: 'FIVE', text: '5', size: 1 },
                { checked: false, value: 'SIX', text: '6', size: 1 },
                { checked: false, value: 'SEVEN', text: '7', size: 1 },
                { checked: false, value: 'EIGHT', text: '8', size: 1 },
                { checked: false, value: 'NINE', text: '9', size: 1 },
                { checked: false, value: 'ZERO', text: '0', size: 1 },
                { checked: false, value: 'MINUS', text: '-', size: 1 },
                { checked: false, value: 'EQUALS', text: '=', size: 1 },
                { checked: false, value: 'BACKSPACE', text: 'Back', size: 2 },
            ],
            [
                { checked: false, value: 'TAB', text: 'Tab', size: 1 },
                { checked: false, value: 'Q', text: 'Q', size: 1 },
                { checked: false, value: 'W', text: 'W', size: 1 },
                { checked: false, value: 'E', text: 'E', size: 1 },
                { checked: false, value: 'R', text: 'R', size: 1 },
                { checked: false, value: 'T', text: 'T', size: 1 },
                { checked: false, value: 'Y', text: 'Y', size: 1 },
                { checked: false, value: 'U', text: 'U', size: 1 },
                { checked: false, value: 'I', text: 'I', size: 1 },
                { checked: false, value: 'O', text: 'O', size: 1 },
                { checked: false, value: 'P', text: 'P', size: 1 },
                { checked: false, value: 'LEFT_BRACKET', text: '[', size: 1 },
                { checked: false, value: 'RIGHT_BRACKET', text: ']', size: 1 },
                { checked: false, value: 'BACKSLASH', text: '\\', size: 1 },
            ],
            [
                { checked: false, value: 'CAPS_LOCK', text: 'Caps Lock', size: 1 },
                { checked: false, value: 'A', text: 'A', size: 1 },
                { checked: false, value: 'S', text: 'S', size: 1 },
                { checked: false, value: 'D', text: 'D', size: 1 },
                { checked: false, value: 'F', text: 'F', size: 1 },
                { checked: false, value: 'G', text: 'G', size: 1 },
                { checked: false, value: 'H', text: 'H', size: 1 },
                { checked: false, value: 'I', text: 'I', size: 1 },
                { checked: false, value: 'J', text: 'J', size: 1 },
                { checked: false, value: 'K', text: 'K', size: 1 },
                { checked: false, value: 'L', text: 'L', size: 1 },
                { checked: false, value: 'SEMICOLON', text: ';', size: 1 },
                { checked: false, value: 'QUOTE', text: '\'', size: 1 },
                { checked: false, value: 'ENTER', text: 'Enter', size: 1 },
            ],
            [
                { checked: false, value: 'LEFT_SHIFT', text: 'Shift', size: 1 },
                { checked: false, value: 'Z', text: 'Z', size: 1 },
                { checked: false, value: 'X', text: 'X', size: 1 },
                { checked: false, value: 'C', text: 'C', size: 1 },
                { checked: false, value: 'V', text: 'V', size: 1 },
                { checked: false, value: 'B', text: 'B', size: 1 },
                { checked: false, value: 'N', text: 'N', size: 1 },
                { checked: false, value: 'M', text: 'M', size: 1 },
                { checked: false, value: 'COMMA', text: ',', size: 1 },
                { checked: false, value: 'PERIOD', text: '.', size: 1 },
                { checked: false, value: 'FORWARD_SLASH', text: '/', size: 1 },
                { checked: false, value: 'RIGHT_SHIFT', text: 'Shift', size: 1 },
            ],
            [
                { checked: false, value: 'LEFT_CONTROL', text: 'Ctrl', size: 1 },
                { checked: false, value: 'LEFT_GUI', text: 'Win', size: 1 },
                { checked: false, value: 'LEFT_ALT', text: 'Alt', size: 1 },
                { checked: false, value: 'SPACE', text: 'Space', size: 5 },
                { checked: false, value: 'RIGHT_ALT', text: 'Alt', size: 1 },
                { checked: false, value: 'RIGHT_GUI', text: 'Win', size: 1 },
                { checked: false, value: 'APPLICATION', text: 'Menu', size: 1 },
                { checked: false, value: 'RIGHT_CONTROL', text: 'Ctrl', size: 1 },
            ],
        ],
        [
            [
                { checked: false, value: 'PRINT_SCREEN', text: 'Prt Scr', size: 1 },
                { checked: false, value: 'SCROLL_LOCK', text: 'Scroll lock', size: 1 },
                { checked: false, value: 'PAUSE', text: 'Pause Break', size: 1 },
            ],
            [
                { checked: false, value: 'INSERT', text: 'Insert', size: 1 },
                { checked: false, value: 'HOME', text: 'Home', size: 1 },
                { checked: false, value: 'PAGE_UP', text: 'Page Up', size: 1 },
            ],
            [
                { checked: false, value: 'DELETE', text: 'Delete', size: 1 },
                { checked: false, value: 'END', text: 'End', size: 1 },
                { checked: false, value: 'PAGE_DOWN', text: 'Page Down', size: 1 },
            ],
            [
                { checked: false, value: 'none', text: 'gap', size: 1 },
            ],
            [
                { checked: false, value: 'none', text: 'gap', size: 1 },
                { checked: false, value: 'UP_ARROW', text: '↑', size: 1 },
                { checked: false, value: 'none', text: 'gap', size: 1 },
            ],
            [
                { checked: false, value: 'LEFT_ARROW', text: '←', size: 1 },
                { checked: false, value: 'DOWN_ARROW', text: '↓', size: 1 },
                { checked: false, value: 'RIGHT_ARROW', text: '→', size: 1 },
            ],
        ],
        [
            [
                { checked: false, value: 'none', text: 'gap', size: 1 },
            ],
            [
                { checked: false, value: 'NUM_LOCK', text: 'NmL', size: 1 },
                { checked: false, value: 'KEYPAD_FORWARD_SLASH', text: '/', size: 1 },
                { checked: false, value: 'KEYPAD_ASTERISK', text: '*', size: 1 },
                { checked: false, value: 'KEYPAD_MINUS', text: '-', size: 1 },
            ],
            [
                { checked: false, value: 'KEYPAD_SEVEN', text: '7', size: 1 },
                { checked: false, value: 'KEYPAD_EIGHT', text: '8', size: 1 },
                { checked: false, value: 'KEYPAD_NINE', text: '9', size: 1 },
                { checked: false, value: 'KEYPAD_PLUS', text: '+', size: 1 },
            ],
            [
                { checked: false, value: 'KEYPAD_FOUR', text: '4', size: 1 },
                { checked: false, value: 'KEYPAD_FIVE', text: '5', size: 1 },
                { checked: false, value: 'KEYPAD_SIX', text: '6', size: 1 },
                { checked: false, value: 'KEYPAD_SIX', text: 'gap', size: 1 },
            ],
            [
                { checked: false, value: 'KEYPAD_ONE', text: '1', size: 1 },
                { checked: false, value: 'KEYPAD_TWO', text: '2', size: 1 },
                { checked: false, value: 'KEYPAD_THREE', text: '3', size: 1 },
                { checked: false, value: 'KEYPAD_ENTER', text: '⤶', size: 1 },

            ],
            [
                { checked: false, value: 'KEYPAD_ZERO', text: '0', size: 1 },
                { checked: false, value: 'KEYPAD_PERIOD', text: '.', size: 1 },
            ]
        ],
    ]);

    return { ADKeys, ActiveKey, fn, SCKeys }
});