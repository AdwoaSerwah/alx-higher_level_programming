#!/usr/bin/node
const { argv } = require('node:process');
let toNum = Number(argv[2]);
if (isNaN(toNum)) console.log('Missing size');
else {
  toNum = Math.floor(toNum);
  for (let j = 0; j < toNum; j++) {
    let str = '';
    for (let i = 0; i < toNum; i++) {
      str += 'X';
    }
    console.log(str);
  }
}
