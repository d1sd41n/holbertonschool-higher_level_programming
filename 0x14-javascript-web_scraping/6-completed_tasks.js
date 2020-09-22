#!/usr/bin/node
const re = require('request');
re.get(process.argv[2], function (error, res, data) {
  if (error) {
    console.log(error);
  } else {
    const dataList = {};
    for (const i of JSON.parse(data)) {
      if (i.completed) {
        if (!dataList[i.userId]) {
          dataList[i.userId] = 1;
        } else {
          dataList[i.userId] += 1;
        }
      }
    }
    console.log(dataList);
  }
});
