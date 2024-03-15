<template>
    <section class="home">
        <select name="selectPot" id="selPot" v-model="GBVar.ADKeys[GBVar.ActiveKey].shuffleAction" @change="UpdateInfo">
            <option :value="['VOLUME_INCREMENT', 'VOLUME_DECREMENT']">Volume control</option>
            <option :value="['BRIGHTNESS_INCREMENT','BRIGHTNESS_DECREMENT']">Brightness control</option>
        </select>
        <button @click="dirChange">
            <p v-if="GBVar.ADKeys[GBVar.ActiveKey].potDir === 'down'">↓</p>
            <p v-if="GBVar.ADKeys[GBVar.ActiveKey].potDir === 'up'">↑</p>
        </button>
        <input
            type="number"
            name="steps"
            min="0"
            max="200"
            onpaste="return false;"
            v-model="GBVar.ADKeys[GBVar.ActiveKey].steps"
            @keypress="blockNumber($event)"
        />
    </section>
</template>
<script setup>
import { ref, onMounted, computed } from 'vue';
import { useGBVar } from '../../stores/GBVariables';
const GBVar = useGBVar();

onMounted(() => {
    UpdateInfo();
});
function UpdateInfo() {
    if (GBVar.ADKeys[GBVar.ActiveKey].shuffleAction.includes('VOLUME_INCREMENT')) {
        GBVar.ADKeys[GBVar.ActiveKey].info = 'Volume control'
    } else if (GBVar.ADKeys[GBVar.ActiveKey].shuffleAction.includes('BRIGHTNESS_INCREMENT')) {
        GBVar.ADKeys[GBVar.ActiveKey].info = 'Brightness control'
    }
}
function dirChange() {
    if (GBVar.ADKeys[GBVar.ActiveKey].potDir === 'down') {
        GBVar.ADKeys[GBVar.ActiveKey].potDir = 'up';
    } else {
        GBVar.ADKeys[GBVar.ActiveKey].potDir = 'down';
    }
}
function blockNumber(event) {
    if (['+', '-', '.'].includes(event.key)) {
        event.preventDefault();
    }
    if (event.key === '0' && event.target.value === '') {
        event.preventDefault();
    }
}
</script>
<style scoped lang="scss">
.home {
    background-color: white;
    border-radius: 5px;
    padding: 10px;
    display: flex;
    flex-direction: row;
    gap: 10px;
    align-items: center;
    justify-content: center;
    flex-wrap: wrap;
}
</style>