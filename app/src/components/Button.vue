<template>
    <button @click=submitForm() class="btn">
        {{ text }}
    </button>
</template>

<script>
export default {
    name: 'Button',
    props: {
        text: String,
        color: String,
        
    },
    methods: {
        submitForm() {
            
        }
    }
}
</script>

<style scoped>

</style>