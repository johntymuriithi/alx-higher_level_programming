#!/usr/bin/node
const { argv } = require('node:process');

console.log(typeof len)
if (len === 2) {
  console.log('No argument');
} else if (len === 3) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
