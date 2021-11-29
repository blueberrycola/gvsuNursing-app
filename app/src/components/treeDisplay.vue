<template>
  <div id = "decision-tree-page" class="bg-blue-200 h-screen w-screen">
      <Header />  

      <button class="absolute right-5 bottom-2 bg-black text-white" @click="storePDF()">Save PDF</button>
    
    
      <ul class="w-25% absolute justify-left">
        <li>
            <button class="bg-blue-400 rounded-lg px-4 py-2 font-bold pt-5 pb-5 pr-5 pl-5" @click="activeSet = 'futurePlans'"><img src="../assets/icons/icons8-plan-64.png"></button>
        </li>
        <li>
            <button class="bg-yellow-100 rounded-lg px-4 py-2 font-bold pt-5 pb-5 pr-5 pl-5" @click="activeSet = 'deliveryFormat'"><img src="../assets/icons/icons8-online-learning-60.png"></button>
        </li>
        <li>
            <button class="bg-purple-300 rounded-lg px-4 py-2 font-bold pt-5 pb-5 pr-5 pl-5" @click="activeSet = 'transferCredits'"><img src="../assets/icons/icons8-scroll-64.png"></button>
        </li>
        <li>
            <button class="bg-red-200 rounded-lg px-4 py-2 font-bold pt-5 pb-5 pr-5 pl-5" @click="activeSet = 'time'"><img src="../assets/icons/icons8-hourglass-64.png"></button>
        </li>
        <li>
            <button class="bg-green-500 rounded-lg px-4 py-2 font-bold pt-5 pb-5 pr-5 pl-5" @click="activeSet = 'financialConsiderations'"><img src="../assets/icons/icons8-money-64.png"></button>
        </li>
        <li>
            <button class="bg-yellow-300 rounded-lg px-4 py-2 font-bold pt-5 pb-5 pr-5 pl-5 focus:outline-none focus:ring-2 focus:ring-black" @click="activeSet = 'organizationalResources'"><img src="../assets/icons/icons8-books-64.png"></button>
        </li>
      </ul>

    
      <futurePlans @update:answer="storeAnswers" v-if="activeSet === 'futurePlans'" /> 
      <deliveryFormat @update:answer="storeAnswers" v-if="activeSet === 'deliveryFormat'" />
      <transferCredits @update:answer="storeAnswers" v-if="activeSet === 'transferCredits'"/>
      <timeWizard @update:answer="storeAnswers" v-if="activeSet === 'time'"/>
      <financialConsiderations @update:answer="storeAnswers" v-if="activeSet === 'financialConsiderations'"/>
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
import jsPDF from 'jspdf'


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

        },
        storePDF(){
            let pdfName = "results";
            var doc = new jsPDF();
            console.log(futurePlansResults);
            if(futurePlansResults.length > 0){
                var splitDoc = doc.splitTextToSize(futurePlansResults, 190);
                doc.setFontSize(20).setFont('times', 'bold');
                doc.text("Future Plans", 10, 10);
                doc.setFontSize(15).setFont('times', 'normal');
                doc.text(splitDoc, 10, 20);
                
                
            }

            if(deliveryFormatResults.length > 0){
                doc.addPage();
                var splitDocOne = doc.splitTextToSize(deliveryFormatResults, 190);
                doc.setFontSize(20).setFont('times', 'bold');
                doc.text("Delivery Format", 10, 10);
                doc.setFontSize(15).setFont('times', 'normal');
                doc.text(splitDocOne, 10, 20);
            }

            if(transferCreditsResults.length > 0){
                doc.addPage();
                var splitDocTwo = doc.splitTextToSize(transferCreditsResults, 190);
                doc.setFontSize(20).setFont('times', 'bold');
                doc.text("Transfer Credits", 10, 10);
                doc.setFontSize(15).setFont('times', 'normal');
                doc.text(splitDocTwo, 10, 20);
            }

            if(timeWizardResults.length > 0){
                doc.addPage();
                var splitDocThree = doc.splitTextToSize(timeWizardResults, 190);
                doc.setFontSize(20).setFont('times', 'bold');
                doc.text("Time Considerations", 10, 10);
                doc.setFontSize(15).setFont('times', 'normal');
                doc.text(splitDocThree, 10, 20);
            }

            if(financialConsiderationsResults.length > 0){
                doc.addPage();
                var splitDocFour = doc.splitTextToSize(financialConsiderationsResults, 190);
                doc.setFontSize(20).setFont('times', 'bold');
                doc.text("Financial Considerations", 10, 10);
                doc.setFontSize(15).setFont('times', 'normal');
                doc.text(splitDocFour, 10, 20);
            }

            if(organizationalResourcesResults.length > 0){
                doc.addPage();
                var splitDocFive = doc.splitTextToSize(organizationalResourcesResults, 190);
                doc.setFontSize(20).setFont('times', 'bold');
                doc.text("Organizational Resources", 10, 10);
                doc.setFontSize(15).setFont('times', 'normal');
                doc.text(splitDocFive, 10, 20);
            }
            

            doc.save(pdfName + ".pdf");
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
/*
.decision-tree-page {
    display: flex;
    width: 100%;
    height: 100%;
    justify-content: center;
}
/*
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





/*li:hover {
    background-color: skyblue;
}

li:focus-visible{
    background-color: skyblue;
}
*/

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

#answers {
    list-style-type: none; 
    line-height: 2;
    justify-content: center;
    border: 1px solid blue;
    margin-bottom: 20px;
    border-radius: 15px;
    cursor: pointer;
}

#answers:hover {
    background-color: skyblue;
}

.box-question {
    margin-top: 20px;
}

.main{
    display: flex;
    width: 100%;
    height: 70%;
    flex-flow: column;
    margin: auto;
}

</style>