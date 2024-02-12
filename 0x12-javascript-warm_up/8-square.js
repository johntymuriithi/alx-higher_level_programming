#!/usr/bin/node
const argv = process.argv;
const arg1 = argv[2];
let i = 0;
const ab = 'X';

if (isNaN(arg1) === true) {
  console.log('Missing size');
} else {
  while (i < arg1) {
    console.log(ab.repeat(arg1));
    i++;
  }
}
