#!/usr/bin/node
const l = process.argv.length;
if (l > 3) {
  console.log('Arguments found');
} else if (l === 3) {
  console.log('Argument found');
} else {
  console.log('No argument');
}
