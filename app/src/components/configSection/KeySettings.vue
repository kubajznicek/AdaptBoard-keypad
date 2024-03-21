<template>
    <section class="keySettings">
        <section class="modules">
            <div v-for="(item, i) in modules" :key="item + i">
                <input type="radio" name="modulesSwitch" :id="'modulesSwitch' + item" :value="item" v-model="sw" @change="handleChange($event)"/>
                <label :for="'modulesSwitch' + item">
                    {{ item }}
                </label>
            </div>
        </section>
        <SettSwitch v-if="sw === 'switch'"/>
        <SettPotmetr v-if="sw === 'pot'"/>
        <SettShuffle v-if="sw === 'shuffle'"/>
        <SettDisplay v-if="sw === 'display'"/>
    </section>
</template>
<script setup>
import { ref, watch } from 'vue';
import SettSwitch from './SettSwitch.vue';
import SettPotmetr from './SettPotmetr.vue';
import SettShuffle from './SettShuffle.vue';
import SettDisplay from './SettDisplay.vue';
import { useGBVar } from '../../stores/GBVariables';
const GBVar = useGBVar();

const modules = ['switch', 'pot', 'shuffle', 'display'];


let sw = ref(GBVar.ADKeys[GBVar.ActiveKey].type);
watch(() => GBVar.ActiveKey, (newVal) => {
  sw.value = GBVar.ADKeys[newVal].type;
});
const handleChange = (event) => {
    sw.value = event.target.value;
    GBVar.ADKeys[GBVar.ActiveKey].type = event.target.value;
};
</script>
<style scoped lang="scss">
.keySettings {
    display: flex;
    flex-direction: column;
    gap: 10px;
    margin: 10px 0px;
    width: 45vw;
}
.modules {
    display: flex;
    gap: 10px;
    // justify-content: space-around;
    margin: 10px 0px;
    > div {
        width: 25%;
        display: flex;
        
        > label {
            width: 100%;
            text-align: center;
        }
    }
    input[type="radio"]:checked + label {
        background-color: #b1b1b1;
    }
    input {
        display: none;
    }
    label {
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