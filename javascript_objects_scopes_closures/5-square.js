#!/usr/bin/node
// define and export class Square that inherits from Rectangle
const Rectangle = require('./4-rectangle'); // import Rectangle class from 4-rectangle.js
module.exports = class Square extends Rectangle { // class Square inherits from Rectangle
  constructor (size) { // constructor  (size)
    super(size, size); // call constructor of Rectangle
  }
};
