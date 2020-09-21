#!/usr/bin/node
const SquareFather = require('./5-square');
module.exports = class Square extends SquareFather {
  constructor (size) {
    super(size, size);
  }

  charPrint (c) {
    if (c === undefined) this.print();
    else {
      for (let i = 0; i < this.width; i++) {
        console.log(c.repeat(this.height));
      }
    }
  }
};
