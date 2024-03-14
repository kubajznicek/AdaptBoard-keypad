<template>
  <main>
  <h1>AdBoard</h1>
  <div class="template">
      <ADBoard_2 />
      <KeySettings />
      <!-- <ADBoard :shortCut="ShortCut"/>
        <div v-if="SCBoard">
          <KeyBoard @shortCut="handleShortCut"/>
        </div> -->
      </div>
    </main>
</template>

<script>
import KeyBoard from './components/keyBoard.vue'
import ADBoard from './components/ADBoard.vue'
import ADBoard_2 from './components/ADBoard_2.vue';
import KeySettings from './components/configSection/KeySettings.vue';

export default {
  components: {
    KeyBoard,
    ADBoard,
    ADBoard_2,
    KeySettings
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
}
.template {
  display: flex;
  // flex-direction: column;
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
