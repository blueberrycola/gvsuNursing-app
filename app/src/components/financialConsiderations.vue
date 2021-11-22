<template>

<div class="flex flex-col w-2/5 relative m-auto text-center bg-salmon shadow-2xl pl-10 pr-10 pb-5 pt-5 border-black border-sm rounded-2xl">
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
                                      bg-red-800
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
                        
                        <textarea v-model="fitb" class="shadow-2xl bg-lightSalmon rounded-xl" rows="4" cols="50" placeholder="Additional details:" ref="fitb"></textarea>
                    </ul>
                </div>
                <div class="box-button pb-10">
                    <button class="hover:bg-blue-200" @click="subtract()">Previous</button>
                    <button v-if="b < questions.length" class="hover:bg-blue-200" @click="add()">Next</button>
                    <button v-if="b === questions.length" class="hover:bg-blue-200" @click="organizeResults()">Check Results</button>
                </div>
            </div>

            <div>
                {{financialConsiderationsAnswers}}
            </div>


      </div>
</template>

<script>
const YESNO = [
    
    {answer: "Yes"},
    {answer: "No"},
    
];
let financialConsiderations = [];
    export default {
        name: 'financialConsiderations',
        data(){
            return{
            a:0,
            b:1,
            fitb:"",
            financialConsiderationsAnswers:financialConsiderations,
            financialConsiderationsResults:[],
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
                
                var index = this.a-1;
                if(financialConsiderations[index] != null || index <= financialConsiderations.length-1) {
                    financialConsiderations[index].fitb = this.fitb
                } else {
                    console.log("null found!");
                    var json = {
                        q:this.a,
                        a:"Additional Detail Question",
                        fitb: this.fitb,
                    }
                    financialConsiderations.push(json);
                }
                //console.log(financialConsiderations);

                this.$emit('update:answer', this.financialConsiderationsAnswers);
                //Done so it doesnt keep the previous answer
                this.fitb = "";
                
                
                
                }   
            },
            subtract(){
            if(this.a > 0){
            this.a -= 1
            this.b -= 1
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
                for(var i = 0; i < financialConsiderations.length; i++) {
                    if(entry.q == financialConsiderations[i].q) {
                        console.log('replace question!')
                        financialConsiderations[i] = entry;
                        replace = true;
                    }
                }
                //Only pushes if it hasnt been replaced.
                if(!replace) {
                    financialConsiderations.push(entry);
                }
                
                this.$emit('update:answer', this.financialConsiderationsAnswers);
                //console.log(financialConsiderations);
            },
            organizeResults(){
                var index = this.a;
                if(financialConsiderations[index] != null || index <= financialConsiderations.length-1) {
                    financialConsiderations[index].fitb = this.fitb
                } else {
                    console.log("null found!");
                    var json = {
                        q:this.a,
                        a:"Fill In The Blank Question",
                        fitb: this.fitb,
                    }
                    financialConsiderations.push(json);
                }

                this.$emit('update:answer', this.financialConsiderationsAnswers);

                this.fitb = "";
                

                if(this.financialConsiderationsAnswers.length == this.questions.length && this.financialConsiderationsResults.length == 0){
                    for(var i = 0; i < this.questions.length; i++){
                        this.financialConsiderationsResults.push(this.questions[i].question);
                        this.financialConsiderationsResults.push(this.financialConsiderationsAnswers[i]);
                    }
                    //console.log(this.financialConsiderationsResults);
                    this.$emit('update:answer', this.financialConsiderationsResults)
                }
            }

        }
    }
</script>