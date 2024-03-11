#!/usr/bin/node
const { argv } = require('node:process');
const len = argv.length;

if (len <= 3) console.log(0);
else {
  const myArray = [];
  for (let i = 2; i < len; i++) {
    const toNum = Math.floor(Number(argv[i]));
    myArray.push(toNum);
  }
  myArray.sort().reverse();
  console.log(myArray[1]);
}
