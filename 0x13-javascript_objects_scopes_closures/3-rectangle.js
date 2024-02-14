#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    const letter = 'X';
    let i = 0;
    while (i < this.height) {
      console.log(letter.repeat(this.width));
      i++;
    }
  }
}

module.exports = Rectangle;
