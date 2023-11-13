#!/usr/bin/node
const myArgs = process.argv.slice(2);
const number = parseInt(myArgs[0]);
if (isNaN(number)) {
  console.log('Not a number');
} else {
  console.log('My number: ' + number);
}
