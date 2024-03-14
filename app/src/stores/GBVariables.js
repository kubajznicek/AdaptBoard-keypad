import { ref } from 'vue';
import { defineStore } from "pinia";

export const useGBVar = defineStore('Variables', () => {
    const name = ref('George');


    let keys = [];
    let f = 20;
    for (let i = 0; i < 5; i++) {
        f -= 4;
        for (let k = 0; k < 4; k++) {
            keys.push({
                id: f,
                type: "switch",
                shortCut: ['LEFT_CONTROL', 'C'],
                ccCode: false,
                shuffleAction: ['VOLUME_INCREMENT', 'VOLUME_DECREMENT'],
                text: "",
                potDir: "up",
                steps: 18,
                display: false,
                info: 'Ctrl + C',
            });
            f++;
        };
        f -= 4;
    };
    const ADKeys = ref(keys)
    const ActiveKey = ref(0);


    return { name, ADKeys, ActiveKey }
});