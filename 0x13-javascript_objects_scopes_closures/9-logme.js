#!/usr/bin/node
let c = 0;
exports.logMe = function count (item) {
  console.log(c + ': ' + item);
  c++;
};
