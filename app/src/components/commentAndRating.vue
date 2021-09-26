<template>
    <div classname="commentRating">
        <header>Leave a Comment and Rating!</header>
        <form>
            <label for="fullname">Full name: </label>
            <input type="text" id="fname" name="fname"><br><br>
            <label for="email">Email: </label>
            <input type="text" id="email" name="email"><br><br>
            <label for="rating">Rating (Scored between 0-10 pts): </label>
            <input type="range" id="rating" name="rating" min="1" max="10"><br><br>
            <label for="nursingreview">Comments: </label>
            <textarea id="nursingreview" name="nursingreview" rows="4" cols="50">
            </textarea><br><br>
            <button @click=submitForm()>
                Submit Review
            </button>
        </form>
    </div>
</template>

<script>
    
    export default {
        name: "commentRating",
        methods: {
        submitForm() {
            var fname = document.getElementById("fname");
            var email = document.getElementById("email");
            var rating = document.getElementById("rating");
            var review = document.getElementById("nursingreview");
            var form = {
                name: fname,
                email: email,
                rating: rating,
                review: review,
            };
            console.log(form);
        }
    }
    }


</script>

<style scoped>
    header {
      display: flex;
      justify-content: space-between;
      align-items: center;
      margin-bottom: 20px;
    }
</style>

