#!/usr/bin/node
const numVar = process.argv[2];
if (!parseInt(numVar) || isNaN(numVar)) {
  console.log('Missing size');
} else {
  for (let i = 0; i < numVar; i++) {
    console.log('X'.repeat(numVar));
  }
}
