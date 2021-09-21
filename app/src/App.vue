<template>
  <div id="app">
    <Homepage/>
    <commentRating/>
    <Button/>

  </div>
</template>

<script>
import commentRating from './components/commentAndRating.vue'
import Button from './components/Button.vue'
import Homepage from './components/homePage.vue'


export default {
  name: 'App',
  components: {
    commentRating,
    Button,
    Homepage
  },
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
