<template>
  <div id="app">
    
    <Questions :questions="Questions"/>
    <Button text="Submit"></Button>

  </div>
</template>

<script>

import Questions from './components/questions.vue'
import Button from './components/Button.vue'


export default {
  name: 'App',
  components: {
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
      //FUTURE PLANS
      {
        id: 1,
        text: 'All questions have moved to treeDisplay.vue, this is now used for homepage',
      }
      //ORGANIZATIONAL RESOURCES
      //todo: Affiliation input, one question per page, progress bar, affiliation, 5 star rating, last updated
      //gvsu branding include but for all, robert talbot gvsu math example https://rtalbert.org/about/, gvsu stock imgs,
      //spam filter, adminstration tool, digital hosting cloud, 



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
