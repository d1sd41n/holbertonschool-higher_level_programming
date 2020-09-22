#!/usr/bin/node
const re = require('request');
const fileSystem = require('fs');
re(process.argv[2], (error, _, body) => {
  if (!error) {
    fileSystem.writeFile(process.argv[3], body, error2 => {
      if (error2) console.log(error);
    });
  } else {
    console.log(error);
  }
});
