#!/usr/bin/node
const myArgs = process.argv.slice(2);
const number = parseInt(myArgs[0]);
if (isNaN(number)) {
  console.log('Missing number of occurrences');
} else {
  for (let i = 0; i < number; i++) {
    console.log('C is fun');
  }
}
