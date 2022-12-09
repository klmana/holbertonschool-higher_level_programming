#!/usr/bin/node
// define and export class Rectangle
module.exports = class Rectangle { // class Rectangle
  constructor (width, height) { // constructor  (width, height)
    if (width > 0 && height > 0) {
      this.width = width;
      this.height = height;
    }
  }
};
