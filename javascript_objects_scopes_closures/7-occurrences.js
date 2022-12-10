#!/usr/bin/node
// function that returns the number of occurrences in a list:
exports.nbOccurences = function (list, searchElement) { // function nbOccurences
  let count = 0;
  for (let i = 0; i < list.length; i++) { // for loop to iterate through list
    if (list[i] === searchElement) { // if list[i] is equal to searchElement then
      count++;
    }
  }
  return count;
};
