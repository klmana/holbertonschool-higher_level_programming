#!/usr/bin/node
// script that gets the contents of a webpage and stores it in a file.

const url = process.argv[2];
const file = process.argv[3];
const fs = require('fs');
const request = require('request');

request(url, function (err, response, body) {
  if (err) {
    console.log(err);
  } else if (response.statusCode === 200) {
    fs.writeFile(file, body, 'utf-8', function (err) {
      if (err) {
        console.log(err);
      }
    });
  } else {
    console.log('Erorr Code:' + response.statusCode);
  }
});
