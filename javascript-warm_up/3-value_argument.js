#!/usr/bin/node
const args = process.argv.slice(2); // get all arguments, excluding the node and script name

if (!args[0]) {
  console.log('No argument');
} else {
  console.log(args[0]);
}
