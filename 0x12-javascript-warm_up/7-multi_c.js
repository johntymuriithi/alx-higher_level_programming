#!/usr/bin/node
const argv = process.argv;
const arg = argv[2];
let i = 0;

if (arg === undefined) {
  console.log('Missing number of occurrences');
} else {
  while (i < arg) {
    console.log('C is fun');
    i++;
  }
}
