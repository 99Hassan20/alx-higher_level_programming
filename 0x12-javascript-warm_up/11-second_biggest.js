#!/usr/bin/node
const args = process.argv.slice(2);
if (args.length === 0 || args.length === 1) {
  console.log(0);
} else {
  const sorted = args.sort((a, b) => a - b);
  const max = parseInt(sorted[sorted.length - 1]);
  for (let i = sorted.length - 1; i >= 0; i--) {
    const value = parseInt(sorted[i]);
    if (parseInt(value) < max) {
      console.log(sorted[i]);
      break;
    }
  }
}
