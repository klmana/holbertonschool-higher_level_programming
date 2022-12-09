#!/usr/bin/node
// script to replace the value 12 with 89:
const myObject = { // create an object
  type: 'object', // key: value
  value: 12
};
console.log(myObject);
console.log(myObject.value); // print the value of the object
myObject.value = 89; // replace the value of the object
console.log(myObject);
console.log(myObject.value); // print the value of the object
