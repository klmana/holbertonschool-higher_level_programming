#!/usr/bin/node
// Prints 3 lines: (like 1-multi_languages.js) but by using an array of string and a loop
const myArray = ['C is fun', 'Python is cool', 'JavaScript is amazing']; // create an array of strings and initialize it
for (let index = 0; index < myArray.length; index++) { // loop through the array of strings
  console.log(myArray[index]); // print the current string
}
