#!/usr/bin/node

const Rectangle = require('./4-Rectangle');
class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }
}

module.exports = Square;
