#!/usr/bin/node

const url = 'https://swapi-api.hbtn.io/api/films/' + process.argv[2];
const re = require('request');

re(url, function (error, res, data) {
  if (res.statusCode === 200) {
    JSON.parse(data).characters.forEach(i => {
      re(i, function (error, res, data) {
        if (res.statusCode === 200) {
          console.log(JSON.parse(data).name);
        } else {
          console.error(error);
        }
      });
    });
  } else {
    console.error(error);
  }
});
