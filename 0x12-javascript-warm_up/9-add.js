#!/usr/bin/node
function add (a, b) {
  return a + b;
}
const myArgs = process.argv.slice(2);
const numberOne = parseInt(myArgs[0]);
const numberTwo = parseInt(myArgs[1]);
console.log(add(numberOne, numberTwo));
