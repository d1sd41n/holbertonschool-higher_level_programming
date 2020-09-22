#!/usr/bin/node

const re = require('request');

re(process.argv[2], function (error, re, data) {
  let aux = 0;
  if (error) {
    console.log(error);
  } else {
    for (const movie of JSON.parse(data).results) {
      for (const character of movie.characters) {
        if (character.includes('18')) {
          aux += 1;
        }
      }
    }
    console.log(aux);
  }
});
