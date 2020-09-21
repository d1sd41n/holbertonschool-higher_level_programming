#!/usr/bin/node
exports.esrever = function (list) {
  const templList = [];

  for (let i = list.length - 1; i >= 0; i--) {
    templList.push(list[i]);
  }

  return templList;
};
