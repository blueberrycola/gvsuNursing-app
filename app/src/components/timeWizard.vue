<template>

<div class="flex flex-col w-2/5 relative m-auto text-center bg-tan shadow-2xl pl-10 pr-10 pb-5 pt-5 border-black border-sm rounded-2xl">
            <div class="center border-black">
            </div>
            <div class="main" v-for="(element, index) in questions.slice(a,b)" :key="index">
                <div class="box-question">
                    <h2 class = "font-bold text-xl pb-8">Question {{a + 1}}/{{questions.length}}
                        <div class="relative pt-1">
                            <div class="overflow-hidden h-2 text-xs flex rounded bg-purple-200">
                                <div
                                    v-bind:style="{
                                        width: b/questions.length*100 + '%' 
                                     }"
                                        class="
                                            shadow-none
                                            flex flex-col
                                            text-center
                                            whitespace-nowrap
                                        text-white
                                        justify-center
                                      bg-yellow-300
                                        "
                                    ></div>
                            </div>
                        </div>
                    </h2>
                    <p class = "pb-10">{{element.question}}</p>
                </div>
                <div class="box-suggestion">
                    <ul class ="flex flex-col w-full justify-center pb-10">
                        <li @click="storeAnswer(b,item.answer)" v-for="(item,index) in element.answers" :key="index">
                            {{item.answer}}
                        </li>
                        
                        <textarea v-model="fitb" class="shadow-2xl bg-blanchedAlmond rounded-xl" rows="4" cols="50" placeholder="Additional details:" ref="fitb"></textarea>
                    </ul>
                </div>
                <div class="box-button pb-10">
                    <button class="hover:bg-blue-200" @click="subtract()">Previous</button>
                    <button class="hover:bg-blue-200" @click="add()">Next</button>
                </div>
            </div>


      </div>
</template>

<script>
const YESNO = [
    
    {answer: "Yes"},
    {answer: "No"},
    
];
let time = [];
    export default {
        name: 'timeWizard',
        data(){
            return{
            a:0,
            b:1,
            fitb:"",
            questions:[
            //
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
            ]
            }
        },
        methods: {
            add(){
                if(this.b < this.questions.length){
                this.a += 1
                this.b += 1
                //After going on to the next question entry is pushed into results
                
                var index = this.a;
                if(time[index] != null) {
                    time[index].fitb = this.fitb
                } else {
                    console.log("null found!");
                    var json = {
                        q:this.a,
                        a:"Additional Detail Question",
                        fitb: this.fitb,
                    }
                    time.push(json);
                }
                console.log(time);
                //Done so it doesnt keep the previous answer
                this.fitb = "";
                
                
                
                }   
            },
            subtract(){
            if(this.a > 0){
            this.a -= 1
            this.b -= 1
            //If user changes mind results are popped() and resubmitted, FIXME: going back gets rid of all questions before that.
            }
            },
            storeAnswer(index, str, fitb) {
                var entry = {
                    q: index,
                    a: str,
                    f: fitb
                }
                var replace = false;
                //Replaces question if already submitted.
                for(var i = 0; i < time.length; i++) {
                    if(entry.q == time[i].q) {
                        console.log('replace question!')
                        time[i] = entry;
                        replace = true;
                    }
                }
                //Only pushes if it hasnt been replaced.
                if(!replace) {
                    time.push(entry);
                }
                
                
                console.log(time);
            }
        }
    }
</script>