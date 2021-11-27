const fs = require('fs');
var posTagger = require( 'wink-pos-tagger' );
var tokenize = require( 'wink-tokenizer' )().tokenize;
var tagger = posTagger();

const data = fs.readFileSync('Lucknow.txt', 'utf8')

const tagArr = tagger.tag(tokenize(data));
//console.log(tagArr);


let keyWord = [];
tagArr.map((e)=>{
    if(e.lemma !== undefined && e.pos === "NN" && e.tag !== "symbol" && e.value !== "pop"){
         keyWord.push(e.lemma);
    }
})

//console.log(keyWord);

let wordMap = [];

for (let i = 0; i < keyWord.length; i++) {
    let currentWordCount = wordMap[keyWord[i]];
    let count = currentWordCount ? currentWordCount : 0;
    wordMap[keyWord[i]] = count + 1;
    }

//console.log(wordMap);
//errCheck(keyWord.join(" "));