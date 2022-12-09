#!/usr/bin/node
// script that prints the addition of 2 integers
const args = process.argv.slice(2); // get all arguments, excluding the node and script name
const a = parseInt(args[0]); // convert to integer
const b = parseInt(args[1]); // convert to integer
if (isNaN(a) || isNaN(b)) { // if either is not a number
  console.log('NaN');
} else {
  console.log(a + b); // print the sum
}
