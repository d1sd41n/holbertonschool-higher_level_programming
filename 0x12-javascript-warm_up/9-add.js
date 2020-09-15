#!/usr/bin/node
function add (a, b) {
  return (a + b);
}
const i = parseInt(process.argv[2]);
const j = parseInt(process.argv[3]);
const res = add(i, j);
console.log(res);
