#!/usr/bin/node
const myArgs = process.argv.slice(2);
const number = parseInt(myArgs[0]);
if (isNaN(number)) {
  console.log('Missing size');
} else {
  for (let i = 0; i < number; i++) {
    console.log('X'.repeat(number));
  }
}
