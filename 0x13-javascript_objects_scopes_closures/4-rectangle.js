#!/usr/bin/node
module.exports = class Rectangle {
  constructor (w, h) {
    if (w <= 0 || w === undefined) {
      return this;
    } else if (h <= 0 || h === undefined) {
      return this;
    } else {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    let i = 0;
    while (i < Math.floor(Number(this.height))) {
      console.log('X'.repeat(Math.floor(Number(this.width))));
      i++;
    }
  }

  rotate () {
    const tmp = this.width;
    this.width = this.height;
    this.height = tmp;
  }

  double () {
    this.width *= 2;
    this.height *= 2;
  }
};
