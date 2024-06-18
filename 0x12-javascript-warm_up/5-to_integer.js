#!/usr/bin/node
const { argv } = require('node:process');
const toStr = Number(argv[2]);

if (isNaN(toStr)) console.log('Not a number');
else console.log('My number: ' + Math.floor(toStr));
