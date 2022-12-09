#!/usr/bin/node
// script that prints x times “C is fun
const args = process.argv.slice(2); // get all arguments, excluding the node and script name
const x = parseInt(args[0]); // convert to integer
if (isNaN(x)) {
  console.log('Missing number of occurrences');
}
for (let i = 0; i < x; i++) {
  console.log('C is fun');
}
