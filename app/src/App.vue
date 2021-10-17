<template>
  <div id="app">
    <div class="container" >
    <treeDisplay />
    </div>
  </div>
</template>

<script>


import treeDisplay from './components/treeDisplay.vue';

export default {
  name: 'App',
  components: {
    treeDisplay
  },
  data(){
    return{
      Questions: []
    }
  },
  created(){
    
      //ORGANIZATIONAL RESOURCES
      //todo: Affiliation input, one question per page, progress bar, affiliation, 5 star rating, last updated
      //gvsu branding include but for all, robert talbot gvsu math example https://rtalbert.org/about/, gvsu stock imgs,
      //spam filter, adminstration tool, digital hosting cloud, 



    
  }
}

</script>

<style>
.app {
  font-family: 'Poppins', sans-serif;
  margin: auto;
  letter-spacing: 2px;
}
</style>
