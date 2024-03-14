<template>
    <form @submit.prevent="">
      <section>
        <section>
          <div class="line" v-for="(line, iL) in keys" :key="iL">
            <div class="key" v-for="(key, iK) in line" :style="{flexGrow: key.size}" :key="'keys' + iK">
              <div v-if="!key.gap">
                <input type="checkbox" v-model="key.checked" :id="'key-' + key.text + iK">
                <label :for="'key-' + key.text + iK">{{ key.text }}</label>
              </div>
              <div v-if="key.gap" class="gap">
              </div>
            </div>
          </div>
        </section>
        <section>
          <div class="line" v-for="(line, iL) in keys1" :key="iL">
            <div class="key" :class="{gap: key.noBtn }" v-for="(key, iK) in line" :style="{flexGrow: key.size} " :key="'keys1' + iK">
              <div v-if="!key.gap">
                <input type="checkbox" v-model="key.checked" :id="'key-' + key.text + iK">
                <label :for="'key-' + key.text + iK">{{ key.text }}</label>
              </div>
              <div v-if="key.noBtn" class="key gap">
              </div>
            </div>
          </div>
        </section>
        <section>
          <div class="line" v-for="(line, iL) in keys2" :key="iL">
            <div class="key" :class="{gap: key.noBtn }" v-for="(key, iK) in line" :style="{flexGrow: key.size} " :key="'keys2' + iK">
              <div v-if="!key.gap">
                <input type="checkbox" v-model="key.checked" :id="'key-' + key.text + iK">
                <label :for="'key-' + key.text + iK">{{ key.text }}</label>
              </div>
              <div v-if="key.noBtn" class="key gap">
              </div>
            </div>
          </div>
        </section>
      </section>
        <button type="button" @click="updateSC">Save ShortCut</button>
    </form>
</template>

<script>
export default {
  name: 'KeyBoard',
  methods: {
    updateSC() {
      let SCKeys = [];
      for (let line in this.keys) {
        for (let key in this.keys[line]) {
          if (this.keys[line][key].checked) {
            this.keys[line][key].checked = false;
            SCKeys.push(this.keys[line][key].value);
          }
        }
      }
      for (let line in this.keys1) {
        for (let key in this.keys1[line]) {
          if (this.keys1[line][key].checked) {
            this.keys1[line][key].checked = false;
            SCKeys.push(this.keys1[line][key].value);
          }
        }
      }
      for (let line in this.keys2) {
        for (let key in this.keys2[line]) {
          if (this.keys2[line][key].checked) {
            this.keys2[line][key].checked = false;
            SCKeys.push(this.keys2[line][key].value);
          }
        }
      }
      if (SCKeys.length !== 0) {
        this.$emit('shortCut', SCKeys);
      }
    }
  },
  data () {
    return {
      keys: {
        "line-0": [
          { checked: false, value: 'ESCAPE', text: 'Esc', size: 1 },
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
        "line-1": [
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
          { checked: false, value: 'BACKSPACE', text: 'BACKSPACE', size: 2 },
        ],
        "line-2": [
          { term: false, value: 'TAB', text: 'Tab', size: 2 },
          { term: false, value: 'Q', text: 'Q', size: 1 },
          { term: false, value: 'W', text: 'W', size: 1 },
          { term: false, value: 'E', text: 'E', size: 1 },
          { term: false, value: 'R', text: 'R', size: 1 },
          { term: false, value: 'T', text: 'T', size: 1 },
          { term: false, value: 'Y', text: 'Y', size: 1 },
          { term: false, value: 'U', text: 'U', size: 1 },
          { term: false, value: 'I', text: 'Y', size: 1 },
          { term: false, value: 'O', text: 'O', size: 1 },
          { term: false, value: 'P', text: 'P', size: 1 },
          { term: false, value: 'LEFT_BRACKET', text: '[', size: 1 },
          { term: false, value: 'RIGHT_BRACKET', text: ']', size: 1 },
          { term: false, value: 'BACKSLASH', text: '\\', size: 2 }
        ],
        "line-3": [
          { term: false, value: 'CAPS_LOCK', text: 'Caps Lock', size: 2 },
          { term: false, value: 'A', text: 'A', size: 1 },
          { term: false, value: 'S', text: 'S', size: 1 },
          { term: false, value: 'D', text: 'D', size: 1 },
          { term: false, value: 'F', text: 'F', size: 1 },
          { term: false, value: 'G', text: 'G', size: 1 },
          { term: false, value: 'H', text: 'H', size: 1 },
          { term: false, value: 'J', text: 'J', size: 1 },
          { term: false, value: 'K', text: 'K', size: 1 },
          { term: false, value: 'L', text: 'L', size: 1 },
          { term: false, value: 'SEMICOLON', text: ';', size: 1 },
          { term: false, value: 'QUOTE', text: '\'', size: 1 },
          { term: false, value: 'ENTER', text: 'Enter', size: 2 }
        ],
        "line-4": [
          { term: false, value: 'LEFT_SHIFT', text: 'Shift', size: 2 },
          { term: false, value: 'Z', text: 'Z', size: 1 },
          { term: false, value: 'X', text: 'X', size: 1 },
          { term: false, value: 'C', text: 'C', size: 1 },
          { term: false, value: 'V', text: 'V', size: 1 },
          { term: false, value: 'B', text: 'B', size: 1 },
          { term: false, value: 'N', text: 'N', size: 1 },
          { term: false, value: 'M', text: 'M', size: 1 },
          { term: false, value: 'COMMA', text: ',', size: 1 },
          { term: false, value: 'PERIOD', text: '.', size: 1 },
          { term: false, value: 'FORWARD_SLASH', text: '/', size: 1 },
          { term: false, value: 'RIGHT_SHIFT', text: 'Shift', size: 2 }
        ],
        "line-5": [
          { term: false, value: 'LEFT_CONTROL', text: 'Ctrl', size: 1 },
          { term: false, value: 'LEFT_GUI', text: 'Win', size: 1 },
          { term: false, value: 'LEFT_ALT', text: 'Alt', size: 1 },
          { term: false, value: 'SPACE', text: 'Space', size: 3 },
          { term: false, value: 'RIGHT_ALT', text: 'Alt', size: 1 },
          { term: false, value: 'RIGHT_GUI', text: 'Win', size: 1 },
          { term: false, value: 'APPLICATION', text: 'Menu', size: 1 },
          { term: false, value: 'RIGHT_CONTROL', text: 'Ctrl', size: 1 },
        ]
      },
      keys1: {
        "line_01": [
          {  checked: false, value: 'PRINT_SCREEN', text: 'Prt Scr', size: 1 },
          { checked: false, value: 'SCROLL_LOCK', text: 'Scroll lock', size: 1 },
          { checked: false, value: 'PAUSE', text: 'Pause Break', size: 1 },
        ],
        "line_02": [
          { checked: false, value: 'INSERT', text: 'Insert', size: 1 },
          { checked: false, value: 'HOME', text: 'Home', size: 1 },
          { checked: false, value: 'PAGE_UP', text: 'Page Up', size: 1 },
        ],
        "line_03": [
          { checked: false, value: 'DELETE', text: 'Delete', size: 1 },
          { checked: false, value: 'END', text: 'End', size: 1 },
          { checked: false, value: 'PAGE_DOWN', text: 'Page Down', size: 1 },
        ],
        "line_04": [
          { checked: false, value: 'PAGE_DOWN', text: '<span>&#x200B;</span>', size: 1 , noBtn: true},
        ],
        "line_05": [
          { checked: false, value: 'UP_ARROW', text: '←', size: 1, noBtn: true},
          { checked: false, value: 'UP_ARROW', text: '↑', size: 1 },
          { checked: false, value: 'UP_ARROW', text: '→', size: 1, noBtn: true},
        ],
        "line_06": [
          { checked: false, value: 'LEFT_ARROW', text: '←', size: 1 },
          { checked: false, value: 'DOWN_ARROW', text: '↓', size: 1 },
          { checked: false, value: 'RIGHT_ARROW', text: '→', size: 1 },
        ]
      },
      keys2: {
        "line_01": [
          { checked: false, value: 'NUM_LOCK', text: 'Num Lock', size: 1, noBtn: true },
        ],
        "line_02": [
          { checked: false, value: 'NUM_LOCK', text: 'Num Lock', size: 1 },
          { checked: false, value: 'KEYPAD_FORWARD_SLASH', text: '/', size: 1 },
          { checked: false, value: 'KEYPAD_ASTERISK', text: '*', size: 1 },
          { checked: false, value: 'KEYPAD_MINUS', text: '-', size: 1 },
        ],
        "line_03": [
          { checked: false, value: 'KEYPAD_SEVEN', text: '7', size: 1 },
          { checked: false, value: 'KEYPAD_EIGHT', text: '8', size: 1 },
          { checked: false, value: 'KEYPAD_NINE', text: '9', size: 1 },
          { checked: false, value: 'KEYPAD_PLUS', text: '+', size: 1 },
        ],
        "line_04": [
          { checked: false, value: 'KEYPAD_FOUR', text: '4', size: 1 },
          { checked: false, value: 'KEYPAD_FIVE', text: '5', size: 1 },
          { checked: false, value: 'KEYPAD_SIX', text: '6', size: 1 },
        ],
        "line_05": [
          { checked: false, value: 'KEYPAD_ONE', text: '1', size: 1 },
          { checked: false, value: 'KEYPAD_TWO', text: '2', size: 1 },
          { checked: false, value: 'KEYPAD_THREE', text: '3', size: 1 },
          { checked: false, value: 'KEYPAD_ENTER', text: 'Enter', size: 1 },
        ],
        "line_06": [
          { checked: false, value: 'KEYPAD_ZERO', text: '0', size: 2 },
          { checked: false, value: 'KEYPAD_PERIOD', text: '.', size: 1 },
        ]
      },
    }
  
  }
}
</script>

<style lang="scss" scoped>
form > section {
  display: flex;
  width: 100%;
  gap: 10px
}
.line {
  display: flex;
  flex-direction: row;
    justify-content: center;
    align-items: center;
    gap: 5px;
    flex-wrap: wrap;
    margin-bottom: 5px;
}
.key {
  height: 100%;
    input[type="checkbox"]:checked + label {
        background-color: #b1b1b1;
    }
     label {
        background-color: #fff;
        border-radius: 5px;
        display: flex;
        flex-direction: column;
        gap: 3px;
        justify-content: center;
        align-items: center;
        transition: all 0.3s ease-in-out;
        padding: 10px;
        flex-grow: 1;

        &:hover {
            background-color: #d4d4d4;
        }
    }
     p {
        font-size: 0.7rem;
    }

    input {
        display: none;
    }
  }
  .gap {
    width: 2px;
    visibility: hidden;
  }
button {
  border: none;
  border-radius: 5px;
  padding: 10px;
  font-size: 1rem;
  cursor: pointer;
  background-color: #d4d4d4;
  transition: all 0.3s ease-in-out;

  &:hover {
    background-color: #8d8d8d;
    color: white;
  }
}
</style>