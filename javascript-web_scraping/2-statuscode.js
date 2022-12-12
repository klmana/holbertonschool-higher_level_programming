#!/usr/bin/node
// script that display the status code of a GET request.

const url = process.argv[2];
const request = require('request');

request.get(url, function (err, response) {
  if (err) {
    console.log(err);
  } else {
    console.log('code: ' + response.statusCode);
  }
});
