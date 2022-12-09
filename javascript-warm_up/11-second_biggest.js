#!/usr/bin/node
// script that searches the second biggest integer in the list of arguments.
const args = process.argv.slice(2); // get all arguments, excluding the node and script name
const numbers = args.map(x => parseInt(x)); // convert to integer and store in array
if (numbers.length <= 1) {
  console.log('0');
} else {
  console.log(secondBiggest(numbers));
} // print the second biggest integer in the list of arguments or 0 if there is no second biggest integer
function secondBiggest (numbers) { // function to compute second biggest integer
  const biggest = Math.max(...numbers); // get the biggest integer
  const index = numbers.indexOf(biggest); // get the index of the biggest integer
  numbers.splice(index, 1); // remove the biggest integer from the array
  return Math.max(...numbers); // get the second biggest integer
}
