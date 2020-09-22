#!/usr/bin/node
const re = require('request');
re(process.argv[2], function (_error, response) {
  console.log('code:', response.statusCode);
});
