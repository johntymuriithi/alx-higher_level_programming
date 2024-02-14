#!/usr/bin/node
const square= require('./5-square');

class Square extends square {
  constructor (size) {
    super(size, size);
  }

  charPrint (ch) {
    let i = 0;
    if (ch === undefined) {
      ch = 'X';
    }
    while (i < this.height) {
      console.log(ch.repeat(this.width));
      i++;
    }
  }
}

module.exports = Square;
