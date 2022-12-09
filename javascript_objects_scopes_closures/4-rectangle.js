#!/usr/bin/node
// define and export class Rectangle
module.exports = class Rectangle { // class Rectangle
  constructor (width, height) { // constructor  (width, height)
    if (width > 0 && height > 0) {
      this.width = width;
      this.height = height;
    }
  }

  print () {
    for (let i = 0; i < this.height; i++) {
      let row = '';
      for (let j = 0; j < this.width; j++) {
        row += 'X';
      }
      console.log(row); // console.log('X'.repeat(this.width));
    }
  }

  // Create an instance method called rotate() that exchanges the width and the height of the rectangle
  rotate () {
    const temp = this.width;
    this.width = this.height;
    this.height = temp;
  }

  // Create an instance method called double() that multiples the width and the height of the rectangle by 2
  double () {
    this.width *= 2;
    this.height *= 2;
  }
};
