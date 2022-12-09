#!/usr/bin/node
// script that prints a square
const args = process.argv.slice(2); // get all arguments, excluding the node and script name
const x = parseInt(args[0]); // convert to integer
if (isNaN(x)) {
  console.log('Missing size');
}
for (let i = 0; i < x; i++) {
  console.log('X'.repeat(x));
}
