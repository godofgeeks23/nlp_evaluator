const request = require('request');
const cheerio = require('cheerio');
const WordPOS = require('wordpos'),

    wordpos = new WordPOS();
var wordMap = {};

const scrap = (error, response, html) => {
    console.log("now entered the block of scrap...");
    if (!error && response.statusCode == 200) {
        const $ = cheerio.load(html);
        // console.log(html);
        const content = $('p');
        // console.log(content.text());
        const wordcontent = content.text();
        const wordArr = wordcontent.split(' ');
        wordpos.getPOS(wordcontent, (arrword) => {
            const word = wordArr.filter((x) => {
                return (arrword.nouns.includes(x) || arrword.rest.includes(x));
            });
            word.sort((a, b) => a[1] - b[1]);
            for (let i = 0; i < word.length; i++) {
                let currentWordCount = wordMap[word[i]];
                let count = currentWordCount ? currentWordCount : 0;
                wordMap[word[i]] = count + 1;
            }
            // console.log(wordMap);
        });
    }
};

const search = "Taj mahal";
search.split(" ").join("_");
request(`https://en.wikipedia.org/wiki/${search}`, scrap);
console.log(wordMap);
