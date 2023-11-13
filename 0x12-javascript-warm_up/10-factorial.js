#!/usr/bin/node
function factorial (n) {
  if (isNaN(n) || n === 1) {
    return 1;
  }
  return n * factorial(n - 1);
}
const myArgs = process.argv.slice(2);
const number = parseInt(myArgs[0]);
console.log(factorial(number));
