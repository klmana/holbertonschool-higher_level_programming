#!/usr/bin/node
// function that converts a number from base 10 to another base passed as argument:
exports.converter = function (base) { // function converter to convert number from base 10 to another base
  return function (num) { // return function to convert number from base 10 to another base
    return num.toString(base); // return num converted to base 
  };
};
