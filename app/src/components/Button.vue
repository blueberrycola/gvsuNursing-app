<template>
    <button @click=onClick() class="btn">
        Button
    </button>
</template>

<script>
export default {
    name: 'Button',
    props: {
        text: String,
        color: String
        
    },
    methods: {
        onClick() {
            console.log('clicc');
        }
    }
}
</script>

<style scoped>

</style>