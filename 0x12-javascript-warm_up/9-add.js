#!/usr/bin/node
const { argv } = require('node:process');
const toNum1 = Math.floor(Number(argv[2]));
const toNum2 = Math.floor(Number(argv[3]));

function add (a, b) { console.log(a + b); }
add(toNum1, toNum2);
