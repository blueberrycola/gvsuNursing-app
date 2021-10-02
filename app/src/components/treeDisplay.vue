<template>
  <div id = "tree">
      <button id="submit">Submit Decisions</button>
      <button id="next">Next Question</button>
      <div id="results"></div>
      <commentRating/>
  </div>
</template>

<script>
import commentRating from './commentAndRating.vue'
export default {
    name: treeDisplay,
    components: {
        commentRating,
    },
}
//Global consts
const treeContainer = document.getElementById('tree');
const resultsContainer = document.getElementById('results');
const submitButton = document.getElementById('submit');
const nextButton = document.getElementById('next');
const YESNO = {
    a: "Yes",
    b: "No"
};
const myQuestions = [
  {
    question: "Do you plan to pursue a graduate degree?",
    answers: YESNO,
    
  },
  {
    question: "Do you have any organizational requirements for future studies?",
    answers: YESNO,
    
  },
  {
    question: "Are you undecided on your future plans at this time?",
    answers: YESNO
    
  },
  {
      question: "Do you have a stable internet connection? Do you like remote learning?",
      answers: YESNO,
  },
  {
      question: "What type of learner are you?",
      answers: {
          a: "Audio",
          b: "Visual",
          c: "Both",
      },
  },
  {
      question: "Do you like group projects?",
      answers: YESNO,
  },
  {
      question: "Do you like enjoy the benefits of online learning but still want some face to face interaction?",
      answers: YESNO,
  },
  {
      question: "What is your age?", //FIXME
      answers: YESNO,
  },
  {
      question: "Do you possess any scholarships?", 
      answers: YESNO,
  },
  {
      question: "Do you finance your own education?", 
      answers: YESNO,
  },
  {
      question: "Do you have any financial loans for college",
      answers: YESNO,
  },
  {
      question: "Repayment terms for loan?",
      answers: YESNO,
  },
  
  {
      question: "Does your employer pay for your college?",
      answers: YESNO,
  },
  {
      question: "Are you a transfer student",
      answers: YESNO,
  },
  {
      question: "Do you have an affiliation or concurrent enrollment agreements",
      answers: YESNO,
  },
  {
      question: "how many liberal arts credits do you have?", //FIXME
      answers: YESNO,
  },
  
  {
      question: "Do prefer the faster paced semesters?",
      answers: YESNO,
  },
  {
      question: "Do you possess a fixed or flexible work schedule?",
      answers: {
          a: "Fixed",
          b: "Flexible",
      },
  }
];


function buildTree() {
    const userInput = [];
    const done = false;
    const i = 0;
    console.log(myQuestions[0])
    
}
function showResults() {

}
//on submit show results
submitButton.addEventListener('click', showResults);


</script>

<style>

</style>