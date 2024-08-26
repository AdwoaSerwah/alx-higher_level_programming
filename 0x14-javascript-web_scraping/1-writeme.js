#!/usr/bin/node

const fs = require('fs');

// Get the file path and string to write from the arguments
const filePath = process.argv[2];
const content = process.argv[3];

// Write the string to the file in utf-8
fs.writeFile(filePath, content, 'utf-8', (err) => {
  if (err) {
    console.log(err);
  }
});
