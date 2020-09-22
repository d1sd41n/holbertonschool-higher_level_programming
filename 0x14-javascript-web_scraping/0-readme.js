#!/usr/bin/node
const fileSystem = require('fs');
fileSystem.readFile(process.argv[2], 'utf-8', (error, data) => {
  if (!error) console.log(data);
  else console.log(error);
});
