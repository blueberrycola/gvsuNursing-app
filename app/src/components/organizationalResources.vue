<template>

<div class="flex flex-col w-2/5 m-auto text-center bg-yellow-300 shadow-2xl pl-10 pr-10 pb- pt-5 border-black border-sm rounded-2xl">
            <div class="center border-black">
                <h2 class = "font-bold text-xl pb-6">Organizational Resources:</h2>
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
                        <li id = "answers" @click="storeAnswer(b,item.answer)" v-for="(item,index) in element.answers" :key="index">
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

let organizationalResources = [];
const YESNO = [
    
    {answer: "Yes"},
    {answer: "No"},
    
];
    export default {
        name: 'organizationalResources',
        data(){
            return{
            a:0,
            b:1,
            fitb:"",
            organizationalResourcesAnswers:organizationalResources,
            organizationalResourcesResults:[],
            questions:[
            //
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
                if(organizationalResources[index] != null || index <= organizationalResources.length-1) {
                    organizationalResources[index].fitb = this.fitb
                } else {
                    console.log("null found!");
                    var json = {
                        q:this.a,
                        a:"Fill In The Blank Question",
                        fitb: this.fitb,
                    }
                    organizationalResources.push(json);
                }
                console.log(organizationalResources);
                
                this.$emit('update:answer', this.organizationalResourcesAnswers);
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
            storeAnswer(index, str) {
                var entry = {
                    q: index,
                    a: str,
                }
                var replace = false;
                //Replaces question if already submitted.
                for(var i = 0; i < organizationalResources.length; i++) {
                    if(entry.q == organizationalResources[i].q) {
                        console.log('replace question!')
                        organizationalResources[i] = entry;
                        replace = true;
                    }
                }
                //Only pushes if it hasnt been replaced.
                if(!replace) {
                    organizationalResources.push(entry);
                }
                
                this.$emit('update:answer', this.organizationalResourcesAnswers);
                //console.log(organizationalResources);
            },
            organizeResults(){
                var index = this.a;
                if(organizationalResources[index] != null || index <= organizationalResources.length-1) {
                    organizationalResources[index].fitb = this.fitb
                } else {
                    console.log("null found!");
                    var json = {
                        q:this.a,
                        a:"Fill In The Blank Question",
                        fitb: this.fitb,
                    }
                    organizationalResources.push(json);
                }
                this.$emit('update:answer', this.organizationalResourcesAnswers);
                this.fitb = "";
                
                if(this.organizationalResourcesAnswers.length == this.questions.length && this.organizationalResourcesResults.length == 0){
                    for(var i = 0; i < this.questions.length; i++){
                        this.organizationalResourcesResults.push((i+1).toString() + ". " + this.questions[i].question);
                        if(this.organizationalResourcesAnswers[i]["a"] != "Fill In The Blank Question")
                            this.organizationalResourcesResults.push("\t"+this.organizationalResourcesAnswers[i]["a"]);
                        if(this.organizationalResourcesResults[i]["fitb"] != "")
                            this.organizationalResourcesResults.push("\t"+this.organizationalResourcesAnswers[i]["fitb"]);
                    }
                    //console.log(this.organizationalResourcesResults);
                    this.$emit('update:answer', this.organizationalResourcesResults);
                }
            }
        }
    }
</script>