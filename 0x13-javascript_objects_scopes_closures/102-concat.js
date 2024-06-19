#!/usr/bin/node
const fs = require('fs');

if (process.argv.length === 5) {
  const [, , fileA, fileB, fileC] = process.argv;
  if (fs.existsSync(fileA) && fs.existsSync(fileB)) {
    const str1 = fs.readFileSync(fileA, 'utf8');
    const str2 = fs.readFileSync(fileB, 'utf8');
    const str3 = str1 + str2;

    fs.writeFileSync(fileC, str3);
  }
}
