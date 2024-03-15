import { ref } from 'vue';
import { defineStore } from "pinia";

export const useGBVar = defineStore('Variables', () => {
    const fn = [
        { action: 'BRIGHTNESS_INCREMENT', info: 'Brightness Up' },
        { action: 'BRIGHTNESS_DECREMENT', info: 'Brightness Down' },
        { action: 'EJECT', info: 'Eject' },
        { action: 'FAST_FORWARD', info: 'fast forward' },
        { action: 'MUTE', info: 'Mute' },
        { action: 'PLAY_PAUSE', info: 'Play/Pause' },
        { action: 'RECORD', info: 'Record' },
        { action: 'REWIND', info: 'Rewind' },
        { action: 'SCAN_NEXT_TRACK', info: 'Next track' },
        { action: 'SCAN_PREVIOUS_TRACK', info: 'Previous track' },
        { action: 'STOP', info: 'Stop' },
        { action: 'VOLUME_DECREMENT', info: 'Volume Down' },
        { action: 'VOLUME_DECREMENT', info: 'Volume Down' },
    ]
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
                action: 'short cut',
                fn: fn[0],
            });
            f++;
        };
        f -= 4;
    };
    const ADKeys = ref(keys)
    const ActiveKey = ref(0);


    return { ADKeys, ActiveKey, fn }
});