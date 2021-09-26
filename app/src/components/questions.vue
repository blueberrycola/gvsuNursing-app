<template>
    <h2>
    <div :key="question.id" v-for="question in questions">
        <Question :question="question"></Question>
        <Radio></Radio>
    </div>
    </h2>

</template>

<script>

    import Question from './question.vue'
    import Radio from './Radio.vue'
    export default {
        name: 'Questions',
        props: {
            questions: Array
        },
        components: {
            Question,
            Radio
        }
    }
</script>
