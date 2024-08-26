#!/usr/bin/node

const fs = require('fs');

// Get the file path from the first argument
const filePath = process.argv[2];

// Read the file content in utf-8
fs.readFile(filePath, 'utf-8', (err, data) => {
  if (err) {
    console.log(err);
  } else {
    console.log(data);
  }
});
