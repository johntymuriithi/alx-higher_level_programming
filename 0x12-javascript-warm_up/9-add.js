#!/usr/bin/node
const argv = process.argv;
const arg1 = argv[2];
const arg2 = argv[3];

function add (a, b) {
  return Number(a) + Number(b);
}
console.log(add(arg1, arg2));
