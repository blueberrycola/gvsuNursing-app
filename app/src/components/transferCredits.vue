<template>

<div class="flex flex-col w-2/5 relative m-auto text-center bg-purple-300 shadow-2xl pl-10 pr-10 pb-5 pt-5 border-black border-sm rounded-2xl">
            <div class="center border-black">
                <h2 class = "font-bold text-xl pb-6">Transfer Credits:</h2>
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
        bg-purple-500
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
                        
                        <textarea v-model="fitb" class="shadow-2xl bg-purple-200 rounded-xl" rows="4" cols="50" placeholder="Additional details:" ref="fitb"></textarea>
                    </ul>
                </div>
                <div class="box-button pb-10">
                    <button class="hover:bg-blue-200" @click="subtract()">Previous</button>
                    <button v-if="b < questions.length" class="hover:bg-blue-200" @click="add()">Next</button>
                    <button v-if="b === questions.length" class="hover:bg-blue-200" @click="organizeResults()">Check Results</button>
                </div>
            </div>


        <div>{{transferCreditsAnswers}}</div>

      </div>
</template>

<script>
const YESNO = [
    
    {answer: "Yes"},
    {answer: "No"},
    
];
let transferCredits = [];
    export default {
        name: 'transferCredits',
        data(){
            return{
            a:0,
            b:1,
            fitb:"",
            transferCreditsAnswers:transferCredits,
            transferCreditsResults:[],
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
                
                }
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
                if(transferCredits[index] != null || index <= transferCredits.length-1) {
                    transferCredits[index].fitb = this.fitb
                } else {
                    console.log("null found!");
                    var json = {
                        q:this.a,
                        a:"Fill In The Blank Question",
                        fitb: this.fitb,
                    }
                    transferCredits.push(json);
                }
                //console.log(transferCredits);
                this.$emit('update:answer', this.transferCreditsAnswers);
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
                for(var i = 0; i < transferCredits.length; i++) {
                    if(entry.q == transferCredits[i].q) {
                        console.log('replace question!')
                        transferCredits[i] = entry;
                        replace = true;
                    }
                }
                //Only pushes if it hasnt been replaced.
                if(!replace) {
                    transferCredits.push(entry);
                }
                
                this.$emit('update:answer', this.transferCreditsAnswers);
                //console.log(transferCredits);
            },
            organizeResults(){
                var index = this.a;
                if(transferCredits[index] != null || index <= transferCredits.length-1) {
                    transferCredits[index].fitb = this.fitb
                } else {
                    console.log("null found!");
                    var json = {
                        q:this.a,
                        a:"Fill In The Blank Question",
                        fitb: this.fitb,
                    }
                    transferCredits.push(json);
                }
            
                this.$emit('update:answer', this.transferCreditsAnswers);
                this.fitb = "";
                
                if(this.transferCreditsAnswers.length == this.questions.length && this.transferCreditsResults.length == 0){
                    for(var i = 0; i < this.questions.length; i++){
                        this.transferCreditsResults.push((i+1).toString() + ". " + this.questions[i].question);
                        if(this.transferCreditsAnswers[i]["a"] != "Fill In The Blank Question")
                            this.transferCreditsResults.push("\t"+this.transferCreditsAnswers[i]["a"]);
                        if(this.transferCreditsResults[i]["fitb"] != "")
                            this.transferCreditsResults.push("\t"+this.transferCreditsAnswers[i]["fitb"]);
                    }
                    console.log(this.transferCreditsResults);
                    this.$emit('update:answer', this.transferCreditsResults);
                }
            }
        }
    }
</script>
