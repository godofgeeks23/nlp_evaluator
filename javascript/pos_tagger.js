// basic POS tagging
// const request = require('request');
// wordpos = new WordPOS();
// var content = 'The angry bear chased the frightened little squirrel.';
// wordpos.getPOS(content, function(result){
//     console.log(result);
// });

const request = require('request');
const cheerio = require('cheerio');
const WordPOS = require('wordpos'),

wordpos = new WordPOS();
var wordMap = {};

const scrap = (error, response, html) => {
    if (!error && response.statusCode == 200) {
        const $ = cheerio.load(html);
        const content = $('p');
        const wordcontent = content.text();
        wordpos.getPOS(wordcontent, function(result){
            console.log(result);
        });
    }
};

const search = "Taj mahal".split(" ").join("_");
request(`https://en.wikipedia.org/wiki/${search}`, scrap);
