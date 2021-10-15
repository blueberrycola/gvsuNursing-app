<template>
  <div id = "decision-tree-page">
      <div class="tree-container">
            <div id="tree-header">
                <h1>Decision Tree</h1>
            </div>
            <div id="main" v-for="(element, index) in questions.slice(a,b)" :key="index">
                <div class="box-question">
                    <h2>Question {{b}}/{{questions.length}}</h2>
                    <p>{{element.question}}</p>
                </div>
                <div class="box-suggestion">
                    <ul>
                        <li v-for="(item,index) in element.answers" :key="index">
                            {{item.answer}}
                        </li>
                    </ul>
                </div>
            </div>
            <div id="tree-footer">
                <div class="box-button">
                    <button>Next</button>
                </div>
            
      </div>


      </div>
      
    
  </div>
  
</template>

<script>
/***************************************************************************
TODO:
    //Quiz Display {Next, Prev, Submit, showResults()}
    //Revise questions (doc posted in capstone shared)
    //Code logic into choosing questions 
    ie: if you prefer online classes then dont suggest in person bsn's
    //Results Display {
        we need data to show different bsn options (strouse or web scraping)

    }
**********************************************************************/
const YESNO = [
    
    {answer: "Yes"},
    {answer: "No"},
    
];

export default {
    name: 'treeDisplay',
    data() {
        return {
        questions:[
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
                answers: [
                    {answer: "Fixed"},
                    {answer: "Flexible"},
                ],
            },
  
                ],
  a:0,
  b:1,
  }
  }
}
/*
//Global consts
const treeContainer = document.getElementById('tree');
const resultsContainer = document.getElementById('results');
const submitButton = document.getElementById('submit');
const nextButton = document.getElementById('next');




function buildTree() {
    const userInput = [];
    const done = false;
    const i = 0;
    console.log(myQuestions[0])
    
}
function showResults() {

}
*/
//on submit show results
//submitButton.addEventListener('click', showResults);


</script>

<style>
.decision-tree-page {
    display: flex;
    width: 100%;
    height: 100%;
    justify-content: center;
}

.tree-container {
    display: flex;
    width: 40%;
    height: 85%;
    position: absolute;
    top: 0;
    bottom: 0;
    margin-top: 40px;
    margin-left: 560px;
    flex-flow: column;
    text-align: center;
    border: 1px solid #e7eae0;
    border-radius: 10px;
    background-color: white;
    box-shadow: 0 10px 20px rgba(0,0,0,0.19), 0 6px 6px rgba(0,0,0,0.23);
}
.tree-header {
    display: flex;
    width: 100%;
    height: 20%;
    border-bottom: 1px solid wheat;
    justify-content: center;
    align-items: center;
    background-color: wheat;
    border-radius: 10px 10px 0px 0px;

}
.main{
    display: flex;
    width: 100%;
    height: 70%;
    flex-flow: column;
    margin: auto;
}
.tree-footer{
    display: flex;
    width: 100%;
    height: 10%;
    justify-content: center;
    border-top: 1px solid skyblue;
    background-color: wheat;
    border-radius: 0px 0px 10px 10px;
}
.box-question {
    margin-top: 20px;
}

.box-suggestions {
    display: flex;
    width: 100%;
    height: 10%;
    justify-content: center;
    border-top: 1px solid wheat;
    background-color: wheat;
    border-radius: 0px 0px 10px 10px;
}
ul{
    display: flex;
    justify-content: center;
    width: 80%;
    margin: 80px;
    padding: 0;
    flex-flow: column;
}
ul li {
    list-style: none;
    line-height: 2;
    justify-content: center;
    border: 1px solid blue;
    margin-bottom: 20px;
    border-radius: 15px;
    cursor: pointer;

}
li:hover {
    background-color: skyblue;
}
.box-button {
    display: flex;
    width: 100%;
}
.box-button button {
    width: 150px;
    height: 35px;
    outline: none;
    border: 0;
    color: white;
    font-size: 18px;
    cursor: pointer;
    border-radius: 15px;
    margin: auto;
    background: grey;
}






</style>