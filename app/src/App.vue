<template>
  <main>
    <h1>AdBoard</h1>
    <div class="template">
      <ADBoard_2 />
      <KeySettings />
        <SCBoard />
    </div>
    <button @click="saveAs">Save as</button>
    </main>
</template>

<script>
import ADBoard_2 from './components/ADBoard_2.vue';
import KeySettings from './components/configSection/KeySettings.vue';
import SCBoard from './components/SCBoard.vue';
import { useGBVar } from './stores/GBVariables';

export default {
  components: {
    ADBoard_2,
    KeySettings,
    SCBoard,
  },
  setup() {
    const GBvar = useGBVar();
    function fileGenerate() {
      let stringFile = 'from adafruit_hid.consumer_control_code import ConsumerControlCode # type: ignore\nfrom adafruit_hid.keycode import Keycode # type: ignore\nfrom micropython import const # type: ignore\n\n';
      // create matrix
      stringFile += 'MATRIX_ACTIONS = {\n';
      for (let i = 0; i < GBvar.ADKeys.length; i++) {
        const key = GBvar.ADKeys[i];
        if (key.type === 'switch') {
          stringFile += `    ${key.id}: lambda cc, kdb, layout: `;
          // if short cut
          if (key.action === 'short cut') {
            stringFile += `kdb.send(`;
            for (let j = 0; j < key.shortCut.length; j++) {
              const element = key.shortCut[j].value;
              stringFile += 'Keycode.' + element;
              if (j != key.shortCut.length - 1) {
                stringFile += ', ';
              }
            }
            stringFile += '),\n';
          }
          // if text
          if (key.action === 'text') {
            stringFile += `layout.write("""${key.text}"""),\n`;
          }
          // FN function
          if (key.action === 'Fn action') {
            stringFile += `cc.send(ConsumerControlCode.${key.fn.action}),\n`;
          }
        }
      }
      stringFile += '}\n\n';
      // create Analog
      stringFile += 'ANALOG_ACTIONS = {\n';
      for (let i = 0; i < GBvar.ADKeys.length; i++) {
        const key = GBvar.ADKeys[i];
        if (key.type === 'shuffle' || key.type === 'pot') {
          stringFile += `    ${key.id - 4}: {\n`;
          stringFile += '        ' + 'True: lambda cc, mouse: cc.send(ConsumerControlCode.' + (key.potDir === 'up' ? String(key.shuffleAction[0]) : String(key.shuffleAction[1])) + '),\n';
          stringFile += '        ' + 'False: lambda cc, mouse: cc.send(ConsumerControlCode.' + (key.potDir === 'up' ? String(key.shuffleAction[1]) : String(key.shuffleAction[0])) + '),\n';
          stringFile += `        "steps": ${key.steps},\n`;
          stringFile += `        "type": "${key.type}",\n`;
          stringFile += `    },\n`;
        }
      }
      stringFile += '}\n\n';

      // display on
      stringFile += 'DISPLAY_CONFIG = {\n    "present": const(';
      for (let i = 0; i < GBvar.ADKeys.length; i++) {
        const key = GBvar.ADKeys[i];
        if (key.type === "display") {
          stringFile += 'True';
          break;
        } else if (i === GBvar.ADKeys.length - 1){
          stringFile += 'False';
        }
      }
      stringFile += '),\n    "WIDTH": const(128),\n    "HEIGHT": const(32),\n}';
      stringFile += '\n\nANALOG_THRESHOLD = const(100)';

      return stringFile;
    }
    async function saveAs() {
      let fileHandle = await window.showSaveFilePicker({
        suggestedName: 'config.py',
        types: [
          {
            description: "Python file",
            accept: {
              "text/plain": [".py"],
            },
          },
        ],
      });
      let stream = await fileHandle.createWritable();
      await stream.write(fileGenerate());
      await stream.close();
    }
    return {fileGenerate, saveAs};
  },
  methods: {
    handleShortCut(data){
      this.ShortCut = data;
    },
  },
  data() {
    return {
      data: '',
      SCBoard: true,
      ShortCut: [],
    }
  }
}
</script>

<style lang="scss" scoped>
main {
  margin: 0px 10px;
  > button {
    margin: 15px 0px;
  }
}
.template {
  display: flex;
  flex-wrap: wrap;
  flex-direction: row;
  gap: 20px;
  justify-content: space-around;
}
h1 {
  color: black;
  font-size: 1.8rem;
  text-align: center;
  margin: 0px;
  padding: 10px;
}
p {
  margin: 0px;
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
