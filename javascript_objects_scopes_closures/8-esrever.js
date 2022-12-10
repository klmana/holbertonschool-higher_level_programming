#!/usr/bin/node
//  function that returns the reversed version of a list:
exports.esrever = function (list) { // function esrever
  const newList = []; // empty array  newList to store reversed list
  for (let i = list.length - 1; i >= 0; i--) { // for loop to iterate through list
    newList.push(list[i]); // push list[i] into newList
  }
  return newList;
};
