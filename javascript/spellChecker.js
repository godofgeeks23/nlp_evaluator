const fs = require('fs');
const spell = require('spell-checker-js')
var posTagger = require( 'wink-pos-tagger' );
var tokenize = require( 'wink-tokenizer' )().tokenize;
var tagger = posTagger();
spell.load('en');

const data = fs.readFileSync('Lucknow.txt', 'utf8')


const check = spell.check(data);
check.toString;
console.log(check);
//const tagArr = tagger.tag(tokenize(check));

let keyWord = [];
tagArr.map((e)=>{
    if(e.value !== undefined && e.pos !== "NN" && e.pos !== "NNP" && e.tag !== "symbol"  && e.tag !== "punctuation" && e.tag !== "number"  && e.value !== "pop"){
         keyWord.push(e.value);
    }
})

console.log(keyWord);
/*const errCheck = (keyWord) =>{
    //console.log(wordMap);
        const check = spell.check(keyWord);
        console.log(check);
}
//errCheck(keyWord);
module.exports = errCheck;*/
