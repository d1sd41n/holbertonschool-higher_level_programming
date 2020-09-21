#!/usr/bin/node

const data = require('./101-data').dict;

const dataObject = {};
for (const i in data) {
  if (dataObject[data[i]]) {
    dataObject[data[i]] = dataObject[data[i]] + ' ' + i;
  } else {
    dataObject[data[i]] = i;
  }
}

for (const i in dataObject) {
  dataObject[i] = dataObject[i].split(' ');
}

console.log(dataObject);
