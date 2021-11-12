<template>

<div class="flex flex-col w-2/5 relative m-auto text-center bg-blue-300 shadow-2xl pl-10 pr-10 pb-5 pt-5 border-black border-sm rounded-2xl">
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
                                            bg-gvsuBlue
                                            pb-8
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
                        
                        <textarea v-model="fitb" class="shadow-2xl bg-blue-200 rounded-xl" rows="4" cols="50" placeholder="Additional details:" ref="fitb"></textarea>
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
</template>

<script>
const YESNO = [
    
    {answer: "Yes"},
    {answer: "No"},
    
];
var entry = {};
let deliveryFormat = [];
    export default {
        name: 'deliveryFormat',
        data(){
            return{
            a:0,
            b:1,
            fitb:"",
            questions:[
            //
            //Orange section (Future Plans)
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
                for(var i = 0; i < deliveryFormat.length; i++) {
                    if(entry.q == deliveryFormat[i].q) {
                        console.log('replace question!')
                        deliveryFormat[i] = entry;
                        replace = true;
                    }
                }
                //Only pushes if it hasnt been replaced.
                if(!replace) {
                    deliveryFormat.push(entry);
                }
                
                
                console.log(deliveryFormat);
            }
        }
    }
</script>