#!/usr/bin/node
function factorial (number) {
  if (!number) {
    return (1);
  } else if (number === 0) {
    return (1);
  } else {
    return (factorial(number - 1) * number);
  }
}
const i = parseInt(process.argv[2]);
const res = factorial(i);
console.log(res);
