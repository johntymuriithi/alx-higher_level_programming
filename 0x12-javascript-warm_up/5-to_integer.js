#!/usr/bin/node
const argv = process.argv;
const arg1 = argv[2];

if (isNaN(arg1) === false) {
  console.log(`My number: ${parseInt(arg1)}`);
} else {
  console.log('Not a number');
}
