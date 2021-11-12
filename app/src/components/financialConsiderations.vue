<template>

<div class="flex flex-col w-2/5 relative m-auto text-center bg-salmon shadow-2xl pl-10 pr-10 pb-5 pt-5 border-black border-sm rounded-2xl">
            <div class="center border-black">
            </div>
            <div class="main" v-for="(element, index) in questions.slice(a,b)" :key="index">
                <div class="box-question">
                    <h2 class = "font-bold text-xl pb-8">Question {{a + 1}}/{{questions.length}}</h2>
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
                                      bg-red-800
                                        "
                                    ></div>
                            </div>
                        </div>
                    <p class = "pb-10">{{element.question}}</p>
                </div>
                <div class="box-suggestion">
                    <ul class ="flex flex-col w-full justify-center pb-10">
                        <li @click="storeAnswer(b,item.answer)" v-for="(item,index) in element.answers" :key="index">
                            {{item.answer}}
                        </li>
                        
                        <textarea v-model="fitb" class="shadow-2xl bg-lightSalmon rounded-xl" rows="4" cols="50" placeholder="Additional details:" ref="fitb"></textarea>
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
var entry = {};
var results = [];
    export default {
        name: 'time',
        data(){
            return{
            a:0,
            b:1,
            fitb:"",
            questions:[
            //
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
            ]
            }
        },
        methods: {
            add(){
                if(this.b < this.questions.length){
                this.a += 1
                this.b += 1
                //After going on to the next question entry is pushed into results
                entry["f"] = this.fitb;
                this.fitb = "";
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
            storeAnswer(index, str, fitb) {
                entry = {
                    q: index,
                    a: str,
                    f: fitb
                }
                console.log(entry);
            }
        }
    }
</script>