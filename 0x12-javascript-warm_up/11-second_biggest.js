#!/usr/bin/node
const argT = process.argv;
const lenArg = argT.length;
if (lenArg < 4) {
  console.log(0);
} else {
  const listrg = argT.slice(2).sort().reverse();
  const num = listrg[1];
  console.log(num);
}
