<template>
  <div id="app">
    <Questions :questions="Questions"/>
    <Button text="Submit"></Button>
    <commentRating/>

  </div>
</template>

<script>
import commentRating from './components/commentAndRating.vue'
import Questions from './components/questions.vue'
import Button from './components/Button.vue'


export default {
  name: 'App',
  components: {
    commentRating,
    Questions,
    Button,
  },
  data(){
    return{
      Questions: []
    }
  },
  created(){
    this.Questions = [
      {
        id: 1,
        text: 'Do you plan to pursue a graduate degree?',
      },
      {
        id: 2,
        text: 'Do you have any organizational requirements for future studies?'
      },
      {
        id: 3,
        text: 'Are you undecided on your future plans at this time?'
      }
    ]
  }
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
