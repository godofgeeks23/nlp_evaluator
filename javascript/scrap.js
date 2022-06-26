const request = require('request');
const cheerio = require('cheerio');
const WordPOS = require('wordpos'),
    wordpos = new WordPOS();
const fs = require('fs');    



const scrap = (error,response,html) => {
    if(!error && response.statusCode == 200){
        const $ = cheerio.load(html);
        //console.log(html);
        const content = $('p');
        //console.log(content.text());
        const wordcontent = content.text().toString();
        fs.writeFile(`${search}.txt`, wordcontent, err => {
            if (err) {
              console.error(err)
            }
          })
    }}
const search = "Lucknow";
search.split(" ").join("_");
request(`https://en.wikipedia.org/wiki/${search}`,scrap);

