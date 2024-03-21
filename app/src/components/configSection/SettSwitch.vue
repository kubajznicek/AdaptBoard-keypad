<template>
    <section class="home">
        <section class="modules">
            <div v-for="(item, i) in functions" :key="item + i">
                <input type="radio" name="fceSwitch" :id="'fceSwitch' + item" v-model="GBVar.ADKeys[GBVar.ActiveKey].action" :value="item" @change="updateInfo">
                <label :for="'fceSwitch' + item">{{ item }}</label>
            </div>
        </section>
        <section v-if="GBVar.ADKeys[GBVar.ActiveKey].action === 'text'">
            <textarea name="textArea" id="" cols="30" rows="3" onpaste="return false" v-model="GBVar.ADKeys[GBVar.ActiveKey].text" @input="updateInfo" @keypress="blockString($event)"></textarea>
        </section>
        <section v-if="GBVar.ADKeys[GBVar.ActiveKey].action === 'Fn action'">
            <select name="FnAction" @change="updateInfo" v-model="GBVar.ADKeys[GBVar.ActiveKey].fn" >
                <option v-for="fce in GBVar.fn" :key="fce" :value="fce">{{ fce.info }}</option>
            </select>
        </section>
        <section v-if="GBVar.ADKeys[GBVar.ActiveKey].action === 'short cut'" class="ShCut">
            <section><p>Aktualni zkratka: </p><p>{{GBVar.ADKeys[GBVar.ActiveKey].info}}</p></section>
            <button @click="newShFce()">Přepsat zkratku</button>
        </section>
    </section>
</template>
<script setup>
import { onMounted, watch } from 'vue';
import { useGBVar } from '../../stores/GBVariables';
const GBVar = useGBVar();

const functions = ['text', 'short cut', 'Fn action'];

onMounted(() => {
    updateInfo();
});
function blockString(event) {
    // if (event.key === '"') {
    //     event.preventDefault();
    // }

    const blocked = [ '"', 'Ě', 'ě', 'Š', 'š', 'Č', 'č', 'Ř', 'ř', 'Ž', 'ž', 'Ý', 'ý', 'Á', 'á', 'Í', 'í', 'É', 'é', 'Ú', 'ú', 'Ů', 'ů', 'Ó', 'ó', 'Ď', 'ď', 'Ť', 'ť', 'Ň', 'ň']
    if (blocked.includes(event.key)) {
        event.preventDefault();
    }
}
function updateInfo() {
    if (GBVar.ADKeys[GBVar.ActiveKey].action === 'text') {
        GBVar.ADKeys[GBVar.ActiveKey].ccCode = false;
        GBVar.ADKeys[GBVar.ActiveKey].info = 'Text: ' + GBVar.ADKeys[GBVar.ActiveKey].text;
    } else if (GBVar.ADKeys[GBVar.ActiveKey].action == 'short cut') {
        GBVar.ADKeys[GBVar.ActiveKey].ccCode = false;
        ShInfo();
    } else if (GBVar.ADKeys[GBVar.ActiveKey].action == 'Fn action') {
        GBVar.ADKeys[GBVar.ActiveKey].info = 'Fn action: ' + GBVar.ADKeys[GBVar.ActiveKey].fn.info;
        GBVar.ADKeys[GBVar.ActiveKey].ccCode = true;
    }
};
function ShInfo() {
    GBVar.ADKeys[GBVar.ActiveKey].info = '';
    for (let i = 0; i < GBVar.ADKeys[GBVar.ActiveKey].shortCut.length; i++) {
        GBVar.ADKeys[GBVar.ActiveKey].info += GBVar.ADKeys[GBVar.ActiveKey].shortCut[i].text
        if (i < GBVar.ADKeys[GBVar.ActiveKey].shortCut.length - 1) {
            GBVar.ADKeys[GBVar.ActiveKey].info += ' + ';
        }
    }
};
function newShFce() {
    const workVar = [];
    for (let i = 0; i < GBVar.SCKeys.length; i++){
        for (let k = 0; k < GBVar.SCKeys[i].length; k++) {
            for (let o = 0; o < GBVar.SCKeys[i][k].length; o++) {
                const key = GBVar.SCKeys[i][k][o];
                if (key.checked) {
                    workVar.push({value: key.value, text: key.text});
                    key.checked = false;
                }
            }
        }
    }
    if (workVar.length != 0) {
        GBVar.ADKeys[GBVar.ActiveKey].shortCut = workVar
        ShInfo();
    }
}
watch(() => GBVar.$state.ActiveKey, (newVal, oldVal) => {
});
</script>
<style scoped lang="scss">
.home {
    background-color: white;
    border-radius: 5px;
    padding: 10px;
    display: flex;
    flex-direction: column;
    gap: 10px;
    align-items: center;
}
.modules {
    display: flex;
    gap: 10px;
    justify-content: space-around;
    margin: 10px 0px;
    
    input[type="radio"]:checked + label {
        background-color: #b1b1b1;
    }
    input {
        display: none;
    }
    label {
        outline: solid 1.5px #b1b1b1;
        border: none;
        padding: 10px;
        border-radius: 5px;
        background-color: #fff;
        transition: all 0.3s ease-in-out;
        &:hover {
            background-color: #d4d4d4;
        }
    }
}
.ShCut {
    display: flex;
    flex-direction: column;
    gap: 5px;
    > section {
        display: flex;
        gap: 5px;
        > p:last-child {
            font-weight: bold;
        }
    }
}
textarea {
    border: 1px solid #d4d4d4;
    border-radius: 5px;
    padding: 5px;
    font-size: 1rem;
    font-family: "Roboto", sans-serif;
    &:active,
    &:focus {
        outline: none;
        box-shadow: none;
    }
}   
</style>