#!/usr/bin/node
const args = process.argv.slice(2); // get all arguments, excluding the node and script name

// If there are less than 2 arguments, just print an empty string
if (args.length < 2) {
  console.log("");
} else {
  // Print the first argument, followed by " is ", followed by the second argument
  console.log(`${args[0]} is ${args[1]}`);
}
