#!/usr/bin/node
const Rectangle = require('./4-rectangle');

class Square extends Rectangle {
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
