#!/usr/bin/node
exports.esrever = function (list) {
  let len = list.length - 1;
  const newArr = [];

  while (len > 0) {
    newArr.push(list[len]);
    len--;
  }
  return newArr;
};
