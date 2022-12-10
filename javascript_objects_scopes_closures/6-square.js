#!/usr/bin/node
// class Square that defines a square and inherits from Square of 5-square.js:
// - instance method called charPrint(c) that prints the rectangle using the character c

const Square5 = require('./5-square'); // import class Square from 5-square.js

module.exports = class Square extends Square5 { // class Square inherits from Square5
  charPrint (c) { // instance method charPrint(c)
    if (c === undefined) { // if c is undefined
      c = 'X'; // set c to 'X'
    }
    for (let i = 0; i < this.height; i++) { // loop through height
      let row = ''; // create empty string row
      for (let j = 0; j < this.width; j++) { // loop through width
        row += c; // add c to row
      }
      console.log(row); // print row
    }
  }
};
