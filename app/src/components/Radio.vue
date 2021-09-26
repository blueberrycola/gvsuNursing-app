<template>
    <div>
        
        <input type="radio" id="yes" value="Yes" v-model="picked">
        <label for="yes">Yes</label>
        <br>
        <input type="radio" id="no" value="No" v-model="picked">
        <label for="no">No</label>
        <br>

    </div>

</template>

<script>
    export default {
        name: 'Radio',
        props: {
            answer: String
        },
        
    }


</script>