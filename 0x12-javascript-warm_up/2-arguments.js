#!/usr/bin/node
const { argv } = require('node:process');
const len = argv.length;

if (len === 1) {
  console.log('No argument');
} else if (len === 2) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
