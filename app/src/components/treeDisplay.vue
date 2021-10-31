<template>
  <div id = "decision-tree-page">
      <Header />
      <div class="flex flex-col w-2/5 relative m-auto text-center bg-white shadow-2xl pl-10 pr-10 pb-5 pt-5 border-black border-sm rounded-2xl">
            <div class="center border-black">
            </div>
            <div class="main" v-for="(element, index) in questions.slice(a,b)" :key="index">
                <div class="box-question">
                    <h2 class = "font-bold text-xl pb-8">Question {{a + 1}}/{{questions.length}}</h2>
                    <p class = "pb-10">{{element.question}}</p>
                </div>
                <div class="box-suggestion">
                    <ul class = "flex flex-col w-full justify-center pb-10">
                        <li v-on:click="storeAnswer(b,item.answer, fitb)" v-for="(item,index) in element.answers" :key="index">
                            {{item.answer}}
                            
                        </li>
                        
                        <textarea v-model="fitb" class="border-b-2 shadow-2xl bg-gray-100" rows="4" cols="50" placeholder="Additional details:">

                        </textarea>
                    </ul>
                </div>
                <div class="box-button pb-10">
                    <button class="hover:bg-blue-200" @click="subtract()">Previous</button>
                    <button class="hover:bg-blue-200" @click="add()">Next</button>
                </div>
            </div>
            <div id="tree-footer">
                     


            </div>


      </div>
      
    
  </div>
  
</template>

<script>
/***************************************************************************
TODO:
    //Quiz Display { showResults()}
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
var entry = null;
//Global array for storing user answers and what question they did
var results = [];
import Header from "./Header.vue"
export default {
    name: 'treeDisplay',
    components: {
        Header
    },
        data() {
        return {
        a:0,
        b:1,
        fitb:"",
        //fitb:document.getElementById("fitb").textContent,
        questions:[
            //
            //Orange section (Future Plans)
            {
                question: "Are you considering continuing your education at the graduate level, and earning an MSN, DNP, or PHD?",
                answers: YESNO,
        
            },
            {
                question: "Does your employer or prospective employer require you to earn your BSN from an accredited program?",
                answers: YESNO,
                
            },
            //
            //Blue section (Delivery Format)
            {
                question: "Are you comfortable and adept at using technology, and do you have the necessary tools to learn online, including an up-to-date computer, software, and internet connection?",
                answers: YESNO
                
            },
            {
                question: "Do you work better with self-scheduling or set schedules?",
                answers: [
                    {answer: "Self-scheduling"},
                    {answer: "Set scheduling"},
                ],
            },
            {
                question: "What type of learner are you?",
                answers: [
                    {answer: "Audio"},
                    {answer: "Visual"},
                    {answer: "Both"},
                ],
            },
            {
                question: "Do you prefer working alone and completing your work at your own rate?",
                answers: YESNO,
            },
            {
                question: "Are there group projects required in my required courses? If so, how will I collaborate with other students in completing these requirements?",
                answers: YESNO,
            },
            //
            //Purple section (Transfer Credits)
            {
                question: "Will credits from my ADN program transfer to the program of interest? If so, how many credits transfer?", 
                answers: YESNO,
            },
            {
                question: "What other general education courses will I need to take to fulfill graduation requirements?", 
                
            },
            {
                question: "Is there an affiliation or concurrent enrollment agreement between my ADN program and other RN to BSN program? How do I participate in these programs?", 
                answers: YESNO,
                //todo: needs elaboration
            },
            //
            //Tan section (Time)
            {
                question: "Are the courses four to eight weeks in length (half a semester) or a full traditional semester or term length (semesters are typically 15 weeks in length)?",
                answers: [
                    {answer: "Four to Eight Weeks"},
                    {answer: "Full 15 Week Semester"}
                ],
            },
            {
                question: "If taking online classes, are there synchronous class sessions that are mandatory to attend? If so, will my work schedule or other responsibilities interfere with this type of class format?",
                answers: YESNO,
            },
            
            {
                question: "What are the application deadlines and costs? What do I need to submit for a complete application? How does this fit with my personal timeline?",
                //Todo: Figure out how to answer / quantify this question
            },
            {
                question: "Is my work schedule flexible or fixed?",
                answers: [
                    {answer: "Flexible"},
                    {answer: "Fixed"},
                ],
            },
            {
                question: "Will I be able to commute to campus regularly for face-to-face courses, and how much time does the commute require?",
                answers: YESNO,
                //Todo: commute time answer
            },
            {
                question: "What family or social responsibilities will be competing for my time in completing my coursework? What support systems do I have that can assist in my success in the program? Can any of my responsibilities be modified or incorporated into my coursework?", //FIXME
                //Todo: figure out how to quantify this               
            },
            //
            //Salmon Section (Financial Considerations)
            {
                question: "How will you finance your education if you plan to pay for it yourself?",
                //Todo: fill in the blank section
            },
            {
                question: "What scholarships or loans are available to help finance my education and what are their requirements/timelines?",
                //Todo: fill in the blank section
            },
            {
                question: "How are courses reimbursed if paid for by employer? What are the requirements, documents, or timelines to consider?",
                //Todo: fill in the blank section
            },
            {
                question: "For employer paid benefits, is there a repayment term if you do not complete your degree?",
                //Todo: fill in the blank section
            },
            {
                question: "Is there a work requirement for every semester you receive tuition reimbursement? If so, do you need to stay in the same role or can you change roles with your new degree?",
                answers: YESNO,
                //Todo: fill in the blank section
            },
            //
            //Yellow Section (Organizational Resources)
            {
                question: "What type of academic support (writing, tutoring, etc.) is available and how is it delivered (on site, online, combination)?",
                //Todo: fill in the blank section
            },
            {
                question: "Who is my advisor, and do I keep a consistent advisor throughout the program? How often do I meet with my advisor?",
                //Todo: fill in the blank section
            },
            {
                question: "Does this university or school offer support to Veterans?",
                answers: YESNO,
            },
            {
                question: "What types and formats of support are available to students with known or suspected disabilities? How do I access these supports?",
                //Todo: fill in the blank section
            },
            {
                question: "Are there identity support groups available that fit my identity? How do I become involved in these groups?",
                answers: YESNO,
                //Todo: fill in the blank section
            },
            {
                question: "What type and when is technology support available? Are there technology requirements for the university or nursing program? What type of computer, software, or internet access do I need to be successful?",
                //Todo: fill in the blank section
            },
            {
                question: "What type of LMS does this school use? Am I familiar with it and if not, what types of tutorial/support is available to help learn the LMS?",
                //Todo: fill in the blank section
            },
            {
                question: "What are the clinical or experiential learning experiences? How many credits or hours are required each semester, and what types of settings are used for these experiences? Are the preceptors or locational provided for me or do I need to secure them?",
                //Todo: fill in the blank section
            },
  
            ],
            
        }
    },
    methods: {
        async created(){
            console.log(this.data())
        },
        add(){
            if(this.b < this.questions.length){
            this.a += 1
            this.b += 1
            //After going on to the next question entry is pushed into results
            results.push(entry);
            console.log(results)
            }
        },
        subtract(){
            if(this.a > 0){
            this.a -= 1
            this.b -= 1
            //If user changes mind results are popped() and resubmitted, FIXME: going back gets rid of all questions before that.
            results.pop();
            }
        },
        //Pushes user choice in results global array. SEE LINE 15
        //FIXME: 
        storeAnswer(index, str, fitb) {
            entry = {
                q: index,
                a: str,
                f: fitb
            }
            console.log(entry);
        },


    },
}
/*
//Global consts
const treeContainer = document.getElementById('tree');
const resultsContainer = document.getElementById('results');
const submitButton = document.getElementById('submit');
const nextButton = document.getElementById('next');
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

li:focus {
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