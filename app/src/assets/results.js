//This javascript file is responsible for taking user input and quantifying it into
//Into the results page

//IMPORTANT: Answers are organized by an array of strings that are parsed by ':'
//the lhs of : is the question number, the rhs is the responce
class Result {
    constructor() {
        this.entry = {
            orange: {
                answers: [],
            },
            blue: {
                answers: [],
            },
            purple: {
                answers: [],
            },
            tan: {
                answers: [],
            },
            salmon: {
                answers: [],
            },
            yellow: {
                answers: [],
            },
        };
    }
    
    
    getAnswer(section, index) {
        var answer = entry[section].answers[index];
        answer = answer.split(':');
        answer = answer[1];
        console.log(answer);
    }
    
    setAnswer(section, responce) {
        entry[section].answers.push(responce);
        console.log(entry)
    }
    
    //loop thru array until lhs number matches and replace rhs with responce
    replaceAnswer(section, responce) {
        var temp = entry[section].answers;
        var parsed = responce.split(':');
        console.log(parsed)
        for(var i = 0; i < temp.length; i++) {
            var old = temp[i].split(':');
            //If question number found replace, ie: 0:'Sample Text'
            if(old[0] == parsed[0]) {
                //Replace old answer with new one in entry obj
                old[1] = parsed[1];
                entry[section].answers.splice(i, 1);
                var newanswer = old[0] + ':' + old[1];
                entry[section].answers.push(newanswer)
    
            }
        }
    }
}

//Entry.js has a json obj used for every user. It has setters (setAnswer, replaceAnswer,)
//It has a getter, and functions to quantify each section and it's answers.

//Testing functions
//setAnswer('orange', '0:foo')
//replaceAnswer('orange', '0:fooo');
//getAnswer('orange', 0);
export default Results;
