#!/usr/bin/node
// function that prints the number of arguments already printed and the new argument value.
let count = 0; // variable count to store number of arguments already printed
exports.logMe = function (item) { // function logMe to print number of arguments already printed and the new argument value
  console.log(count + ': ' + item); // print count and item to console
  count++; // increment count by 1
};
