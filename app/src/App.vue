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
      //FUTURE PLANS
      {
        id: 1,
        text: 'Do you plan to pursue a graduate degree?',
      },
      {
        id: 2,
        text: 'Do you have any organizational requirements for future studies?'
      },
      //FORMAT
      {
        id: 3,
        text: 'Are you undecided on your future plans at this time?'
      },
      {
        id: 4,
        text: 'Do you have a stable internet connection? Do you like remote learning?'
      },
      {
        id: 5,
        text: 'What type of learner are you?' //add input audio/visual, both
      },
      {
        id: 6,
        text: 'Do you like group projects?'
      },
      {
        id: 7,
        text: 'Do you like enjoy the benefits of online learning but still want some face to face interaction?'
      },
      //ETC
      {
        id: 8,
        text: 'What is your age?'
      },
      
      
      //FINANCE
      {
        id: 12,
        text: 'Do you possess any scholarships?'
      },
      {
        id: 13,
        text: 'Do you finance your own education'
      },
      {
        id: 14,
        text: 'Do you have any financial loans for college'
      },
      {
        id: 15,
        text: "Repayment terms for loan"
      },
      {
        id: 16,
        text: "Does your employer pay for your college?"
      },
      //Transfer Credits
      {
        id: 17,
        text: 'Are you a transfer student'
      },
      {
        id: 18,
        text: 'Do you have an affiliation or concurrent enrollment agreements'
      },
      {
        id: 19,
        text: 'Are you okay with all the gen-ed courses you will take?'
      },
      //TIME
      {
        id: 11,
        text: 'Do prefer the faster paced semesters?'
      },
      {
        id: 12,
        text: 'Do you possess a fixed or flexible work schedule?'
      },
      //ORGANIZATIONAL RESOURCES
      



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
