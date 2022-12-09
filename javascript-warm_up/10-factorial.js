#!/usr/bin/node
// script that computes and prints a factorial
const args = process.argv.slice(2); // get all arguments, excluding the node and script name
const number = parseInt(args[0]); // convert to integer
if (isNaN(number)) {
  console.log('1');
} else {
  console.log(factorial(number));
} // print the factorial  of number  or 1 if number is not a number or 0
function factorial (number) { // function to compute factorial
  if (number === 0) {
    return 1;
  } else {
    return number * factorial(number - 1);
  }
}
