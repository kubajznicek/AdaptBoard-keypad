<template>
    <section class="home">
        <div v-for="(sec, p) in GBVar.SCKeys" :key="sec +p">
            <div v-for="(line, i) in sec" :key="line + i" class="line">
                <div class="key" v-for="(key, j) in line" :key="key + j" :style="{ flexGrow: key.size }">
                    <input type="checkbox" :id="key.value + i + j" v-model="key.checked">
                    <label :for="key.value + i + j" :class="{ gap: key.text === 'gap' }">
                        <p>{{ key.text }}</p>
                    </label>
                </div>
            </div>
        </div>
    </section>
</template>
<script setup>
    import { useGBVar } from '../stores/GBVariables';
    const GBVar = useGBVar();
</script>
<style lang="scss" scoped>
.home {
    display: flex;
    flex-wrap: wrap;
    gap: 8px;
    > div {
        display: flex;
        flex-direction: column;
        gap: 5px;
    }
    .line {
        display: flex;
        flex-wrap: wrap;
        gap: 5px;
    }
    .gap {
        visibility: hidden;
    }
    .key {
        input[type="checkbox"]:checked + label {
        background-color: #b1b1b1;
        }
        input {
            display: none;
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
            &:hover {
                background-color: #d4d4d4;
            }
        }
    }
}
</style>