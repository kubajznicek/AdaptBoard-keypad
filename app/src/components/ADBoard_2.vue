<template>
    <section class="ADBoard">
        <div class="key" v-for="(key, i) in GBVar.ADKeys" :key="key + i">
            <input type="radio" name="radio" :id="'radio' + i" :value="i" v-model="GBVar.ActiveKey">
            <label :for="'radio' + i">
                <h3>{{ key.id }}</h3>  
                <p class="type">{{ key.type }}</p>
                <p class="info">{{ key.info }}</p>
            </label>
        </div>
    </section>
</template>
<script setup>
import { ref } from 'vue';
import { useGBVar } from '../stores/GBVariables';

const GBVar = useGBVar();
console.log(GBVar.ADKeys);
</script>
<style lang="scss">
.ADBoard {
    display: grid;
    grid-template-columns: repeat(4, 1fr);
    grid-template-rows: repeat(5, 1fr);
    gap: 5px;
    width: fit-content;

    .key {
        display: inherit;
        min-width: 120px;
        > input {
            display: none;
        }
        > label {
            background-color: #fff;
            border-radius:5px;
            display: flex;
            flex-direction: column;
            gap: 5px;
            justify-content: space-around;
            align-items: center;
            transition: all 0.3s ease-in-out;
            padding: 5px;

            &:hover {
                background-color: #d4d4d4;
            }
            h3 {
                margin: 3px 0px 0px 0px;
                font-size: 1rem;
            }
            p {
                margin: 0px;
            }
            .type {
                font-size: 0.6rem;
            }
            .info {
                font-size: 0.8rem;
                font-weight: bold;
            }
        }
        > input[type="radio"]:checked + label {
            background-color: #b1b1b1;
        }

    }
}
</style>