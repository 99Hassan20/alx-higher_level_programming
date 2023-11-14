#!/usr/bin/node

const Square_ = require('./5-square');
const Square = class Square extends Square_ {
  charPrint (c) {
    if (typeof (c) === 'undefined') {
      this.print();
      return;
    }
    for (let i = 0; i < this.height; i++) {
      console.log(c.repeat(this.width));
    }
  }
};
module.exports = Square;
