<template>
    <div id="commentRating-page">
        <div id="form-container">
            
            <div class="form-main">
                <h1>Leave a Comment and Rating!</h1>
                <div class="form-header">
                    
                
                </div>
            <form>
                    <h4>Full Name:</h4>
                    <input type="text" id="fname" name="fname">
                    <h4>Email:</h4>
                    <input type="text" id="email" name="email"><br><br>
                    <h4>Rating:</h4>
                    <input type="range" id="rating" name="rating" min="1" max="10"><br><br>
                    <h4>Comments:</h4>
                    <textarea id="nursingreview" name="nursingreview" rows="4" cols="50">
                    </textarea><br><br>
                    <button @click=submitForm()>
                        Submit Review
                    </button>
            </form>
            </div>

        </div>

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
            //Fixme: submit json to S3 Bucket
            console.log(form);
        }
    }
    }

</script>

<style>
    .form-header {
        margin: 10px;
    }
    .commentRating-page{
        display: flex;
        width: 100%;
        height: 100;
        
    }
    .form-container {
        display: flex;
        font-family: 'Poppins', sans-serif;
        width: 40%;
        height: 85%;
        margin-top: 40px;
        margin-left: 560px;
        border: 1px solid;
        box-shadow: 5px 10px black;
    }
    .form-main {
        display: flex;
        align-items: center;
        justify-content: center;
        width: 40%;
        height: 85%;
        margin-top: 40px;
        margin-left: 560px;
        position: absolute;
        flex-flow: column;
        border: 1px solid #e7eae0;
        border-radius: 10px;
        background-color: skyblue;
        box-shadow: 0 10px 20px rgba(0,0,0,0.19), 0 6px 6px rgba(0,0,0,0.23);
    }
    
    .form-header {
        display: flex;
        align-items: center;
        justify-content: center;
        display: flex;
        width: 100%;
        height: 10%;
    }

</style>

