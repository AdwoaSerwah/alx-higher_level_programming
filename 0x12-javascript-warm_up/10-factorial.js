#!/usr/bin/node
const { argv } = require('node:process');
const toNum = Math.floor(Number(argv[2]));

function numFactorial (num) {
  if (num === 1 || isNaN(num)) return 1;
  return (num * numFactorial(num - 1));
}

console.log(numFactorial(toNum));
