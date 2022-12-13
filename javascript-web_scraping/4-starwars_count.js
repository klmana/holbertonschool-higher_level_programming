#!/usr/bin/node
// script that prints the number of movies where the character “Wedge Antilles” is present.

const url = process.argv[2];
const request = require('request');
let count = 0;

request(url, function (err, response, body) {
  if (err) {
    console.log(err);
  } else if (response.statusCode === 200) {
    body = JSON.parse(body);
    for (const film of body.results) {
      for (const character of film.characters) {
        if (character.includes('18')) {
          count++;
        }
      }
    }
    console.log(count);
  } else {
    console.log('Erorr Code:' + response.statusCode);
  }
});
