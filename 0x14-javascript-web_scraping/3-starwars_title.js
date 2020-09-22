#!/usr/bin/node
const re = require('request');
const url = 'https://swapi-api.hbtn.io/api/films/' + process.argv[2];
re(url, function (error, res, data) {
  if (res.statusCode === 200) {
    console.log(JSON.parse(data).title);
  } else {
    console.error(error);
  }
});
