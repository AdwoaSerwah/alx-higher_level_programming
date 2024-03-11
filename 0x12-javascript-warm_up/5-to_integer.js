#!/usr/bin/node
const { argv } = require('node:process');
const toStr = parseInt(argv[2], 10);

if (isNaN(toStr)) console.log('Not a number');
else console.log(toStr);
