<template>
    <h3> {{ question.text }} 
    </h3> 
</template>

<script>

export default {
    name: 'Question',
    props: {
        question : Object

    }
}
</script>
