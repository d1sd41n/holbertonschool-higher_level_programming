#!/usr/bin/node
const url = 'http://swapi.co/api/films/' + process.argv[2];
const re = require('request');
re.get(url, function (error, res, data) {
  if (error) {
    console.log(error);
  } else {
    console.log(JSON.parse(data).title);
  }
});
