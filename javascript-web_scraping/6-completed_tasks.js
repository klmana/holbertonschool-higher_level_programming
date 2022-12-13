#!/usr/bin/node
// script that computes the number of tasks completed by user id.

const request = require('request');
const url = process.argv[2];

request(url, function (error, response, body) {
  if (error) { console.log(error); }
  const object = {};
  body = JSON.parse(body);
  for (let number = 0; number < body.length; number++) {
    const id = body[number].userId;
    const completed = body[number].completed;
    if (completed) {
      if (!object[id]) {
        object[body[number].userId] = 1;
      } else {
        object[body[number].userId] += 1;
      }
    }
  }
  console.log(object);
});
