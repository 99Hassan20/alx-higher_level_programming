#!/usr/bin/node
const args = process.argv.slice(2);
if (args.length === 0 || args.length === 1) {
  console.log(0);
} else {
  let max = parseInt(args[0]);
  let secondMax = max;
  for (let i = 0; i < args.length; i++) {
    if (parseInt(args[i]) >= max) {
      secondMax = max;
      max = parseInt(args[i]);
    }
  }
  console.log(secondMax);
}
