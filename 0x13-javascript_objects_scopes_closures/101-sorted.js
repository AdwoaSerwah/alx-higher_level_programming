#!/usr/bin/node
const dict = require('./101-data').dict;
const newDict = {};

for (const key in dict) {
  const newKey = dict[key];
  if (newKey in newDict) newDict[newKey].push(key);
  else {
    newDict[newKey] = [key];
  }
}
console.log(newDict);
