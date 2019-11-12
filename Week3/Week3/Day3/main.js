var libButton = document.getElementById('lib-button');

var libIt = function() {
    var storyDiv = document.getElementById("story");
    let words = document.getElementsByTagName("input");
    let text = `Dear Dr. ${words[0].value}, <br><br>

I cannot make it to ${words[1].value} this ${words[2].value}. I am very ${words[3].value} and cannot stop ${words[4].value + "ing"} my ${words[5].value}. I have a fever of ${words[6].value} degrees and the doctor ordered me to stay in ${words[7].value} and ${words[8].value} lots of ${words[14].value}. Also, can I have a ${words[9].value} on the essay about pieces of ${words[10].value}? My ${words[11].value} ate it and now I have to start all over.<br><br>


Best ${words[12].value},<br>
-${words[13].value}`
    storyDiv.innerHTML = text;
};

libButton.addEventListener('click', libIt);


/*
Name
location
time
adjective
verb
body part
number
type of furniture
verb
noun
noun
animal
adverb
Name

*/