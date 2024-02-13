#!/usr/bin/node
const argv = process.argv;
let big = 0;

if (argv[2] === undefined) {
  console.log(0);
} else if (argv[3] === undefined) {
  console.log(1);
} else {
  for (const x of argv) {
    if (big < x) {
      big = x;
    }
  }
  console.log(big);
}
