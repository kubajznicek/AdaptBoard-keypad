<template>
  <div class="template">
    <h1>AdBoard</h1>
    <ADBoard :shortCut="ShortCut"/>
    <div v-if="SCBoard">
      <KeyBoard @shortCut="handleShortCut"/>
    </div>
  </div>
</template>

<script>
import KeyBoard from './components/keyBoard.vue'
import ADBoard from './components/ADBoard.vue'
export default {
  components: {
    KeyBoard,
    ADBoard
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
.template {
  display: flex;
  flex-direction: column;
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
