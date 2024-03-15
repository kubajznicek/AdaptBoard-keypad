<template>
    <section class="home">
        <section class="modules">
            <div v-for="(item, i) in functions" :key="item + i">
                <input type="radio" name="fceSwitch" :id="'fceSwitch' + item" v-model="GBVar.ADKeys[GBVar.ActiveKey].action" :value="item" @change="updateInfo">
                <label :for="'fceSwitch' + item">{{ item }}</label>
            </div>
        </section>
        <section v-if="GBVar.ADKeys[GBVar.ActiveKey].action === 'text'">
            <input
            type="text"
            name="textArea"
            autocomplete="off"
            onpaste="return false;"
            v-model="GBVar.ADKeys[GBVar.ActiveKey].text"
            @input="updateInfo()">
        </section>
        <section v-if="GBVar.ADKeys[GBVar.ActiveKey].action === 'Fn action'">
            <select name="FnAction" @change="updateInfo" v-model="GBVar.ADKeys[GBVar.ActiveKey].fn" >
                <option v-for="fce in GBVar.fn" :key="fce" :value="fce">{{ fce.info }}</option>
            </select>
        </section>
    </section>
</template>
<script setup>
import { onMounted, ref } from 'vue';
import { useGBVar } from '../../stores/GBVariables';
const GBVar = useGBVar();

const functions = ['text', 'short cut', 'Fn action'];

onMounted(() => {
    updateInfo();
});
function updateInfo() {
    if (GBVar.ADKeys[GBVar.ActiveKey].action === 'text') {
        GBVar.ADKeys[GBVar.ActiveKey].info = 'Text: ' + GBVar.ADKeys[GBVar.ActiveKey].text;
    } else if (GBVar.ADKeys[GBVar.ActiveKey].action == 'short cut') {
        GBVar.ADKeys[GBVar.ActiveKey].info = 'Short cut: ';
    } else if (GBVar.ADKeys[GBVar.ActiveKey].action == 'Fn action') {
        GBVar.ADKeys[GBVar.ActiveKey].info = 'Fn action: ' + GBVar.ADKeys[GBVar.ActiveKey].fn.info;
    }
}
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
</style>