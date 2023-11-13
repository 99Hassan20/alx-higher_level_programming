#!/usr/bin/node
const args = process.argv.slice(2);
let max;
if (args.length === 0 || args.length === 1) {
  console.log(0);
} else {
  max = parseInt(args[0]);
  for (let i = 0; i < args.length; i++) {
    const value = parseInt(args[i]);
    if (value >= max) { max = value; }
  }
  let secondMax = parseInt(args[0]);
  for (let i = 0; i < args.length; i++) {
    const value = parseInt(args[i]);
    if (value >= secondMax && value < max) { secondMax = value; }
  }
  console.log(secondMax);
}
