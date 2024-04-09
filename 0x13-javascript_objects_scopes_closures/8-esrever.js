#!/usr/bin/node
exports.esrever = function (list) {
  const lenList = list.length - 1;
  const reversedList = [];
  for (let i = lenList; i >= 0; i--) {
    reversedList.push(list[i]);
  }
  return reversedList;
};
