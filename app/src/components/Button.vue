<template>
    <button @click=onClick() class="btn">
        {{ text }}
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