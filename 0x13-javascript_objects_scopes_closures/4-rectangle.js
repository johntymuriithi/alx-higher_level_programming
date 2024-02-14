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

  double () {
    this.height = this.height * 2;
    this.width = this.width * 2;
  }

  rotate () {
    this.height = this.width;
    this.width = this.height * 2;
  }
}

module.exports = Rectangle;
