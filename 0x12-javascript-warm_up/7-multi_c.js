#!/usr/bin/node
const { argv } = require('node:process');
let toNum = Number(argv[2]);
if (isNaN(toNum)) console.log('Missing number of occurrences');
else {
  toNum = Math.floor(toNum);
  for (let i = 0; i < toNum; i++) { console.log('C is fun'); }
}
