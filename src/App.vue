<template>
  <div id="app">
    <commentRating/>
    <Button/>

  </div>
</template>

<script>
import commentRating from './components/commentAndRating.vue'
import Button from './components/Button.vue'

export default {
  name: 'App',
  components: {
    commentRating,
    Button
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
