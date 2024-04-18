<template>
    <section class="home">
        <p>Display turned <span>ON</span></p>
    </section>
</template>
<script setup>
import { onMounted, onUnmounted } from 'vue';
import { useGBVar } from '../../stores/GBVariables';
const GBVar = useGBVar();

onMounted(() => {
    updateInfo();
});
function updateInfo() {
    GBVar.ADKeys[GBVar.ActiveKey].info = 'Display ON';
    GBVar.ADKeys[GBVar.ActiveKey].display = true;
}
onUnmounted(() => {
    GBVar.ADKeys[GBVar.ActiveKey].display = false;});
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
    > p > span {
        font-weight: bold;
    }
}
</style>