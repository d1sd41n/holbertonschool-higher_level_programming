#!/usr/bin/node
const fileSystem = require('fs');
fileSystem.writeFile(process.argv[2], process.argv[3], error => {
  if (error) console.log(error);
});
