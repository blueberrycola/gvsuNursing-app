<template>
  <div id = "decision-tree-page" class="bg-gvsuBlue">
      <Header />  

    
      <button class="bg-gamboge pt-5 pb-5 pr-5 pl-5" @click="activeSet = 'futurePlans', compileData()">Future Plans</button>
      
      <futurePlans @update:answer="storeAnswers" v-if="activeSet === 'futurePlans'" />
    
      <button class="bg-blue-300 pt-5 pb-5 pr-5 pl-5" @click="activeSet = 'deliveryFormat'">Delivery Format</button>
     
      <deliveryFormat @update:answer="storeAnswers" v-if="activeSet === 'deliveryFormat'" />
  
      <button class="bg-purple-300 pt-5 pb-5 pr-5 pl-5" @click="activeSet = 'transferCredits'">Transfer Credits</button>
  
      <transferCredits @update:answer="storeAnswers" v-if="activeSet === 'transferCredits'"/>
      
      <button class="bg-tan pt-5 pb-5 pr-5 pl-5" @click="activeSet = 'time'">Time Considerations</button>
     
      <timeWizard @update:answer="storeAnswers" v-if="activeSet === 'time'"/>
     
      <button class="bg-lightSalmon pt-5 pb-5 pr-5 pl-5" @click="activeSet = 'financialConsiderations'">Financial Considerations</button>

      <financialConsiderations @update:answer="storeAnswers" v-if="activeSet === 'financialConsiderations'"/>
   
      <button class="bg-yellow-300 pt-5 pb-5 pr-5 pl-5 focus:outline-none focus:ring-2 focus:ring-black" @click="activeSet = 'organizationalResources'">Organizational Resources</button>

      <organizationalResources @update:answer="storeAnswers" v-if="activeSet === 'organizationalResources'" />
   
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

//Global array for storing user answers and what question they did
var deliveryFormatResults = [];
var financialConsiderationsResults = [];
var futurePlansResults = [];
var timeWizardResults = [];
var organizationalResourcesResults = [];
var transferCreditsResults = [];
import Header from "./Header.vue"
import futurePlans from "./futurePlans.vue"
import deliveryFormat from "./deliveryFormat.vue"
import transferCredits from "./transferCredits.vue"
import financialConsiderations from "./financialConsiderations.vue"
import timeWizard from "./timeWizard.vue"
import organizationalResources from "./organizationalResources.vue"


export default {
    name: 'treeDisplay',
    components: {
        Header,
        futurePlans,
        deliveryFormat,
        transferCredits,
        timeWizard,
        financialConsiderations,
        organizationalResources

    },
        data() {
        return {
        a:0,
        b:1,
        fitb:"",
        activeSet: ""
        }
    },
    methods: {
        async created(){
            console.log(this.data())
        },

        //Stores all component data into a JSON
        storeAnswers(answers){
            if(this.activeSet == "deliveryFormat"){
                deliveryFormatResults = answers;
                console.log(deliveryFormatResults);
            }
            if(this.activeSet == "financialConsiderations"){
                financialConsiderationsResults = answers;
                console.log(financialConsiderationsResults);
            }
            if(this.activeSet == "futurePlans"){
                futurePlansResults = answers;
                console.log(futurePlansResults);
            }
            if(this.activeSet == "timeWizard"){
                timeWizardResults = answers;
                console.log(timeWizardResults);
            }
            if(this.activeSet == "organizationalResources"){
                organizationalResourcesResults = answers;
                console.log(organizationalResourcesResults);
            }
            if(this.activeSet == "transferCredits"){
                transferCreditsResults = answers;
                console.log(transferCreditsResults);
            }

        }

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
    list-style-type: none; 
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

li:focus-visible{
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