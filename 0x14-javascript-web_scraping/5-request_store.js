#!/usr/bin/node
const fs = require('fs');
const request = require('request');

// Check for the correct number of arguments
if (process.argv.length !== 4) {
  console.error('Usage: ./5-request_store.js <URL> <file_path>');
  process.exit(1);
}

// Get URL and file path from command-line arguments
const url = process.argv[2];
const filePath = process.argv[3];

// Make the HTTP request
request(url, (error, response, body) => {
  if (error) {
    console.error('Error fetching the URL:', error);
    process.exit(1);
  }

  // Write the response body to the specified file with UTF-8 encoding
  fs.writeFile(filePath, body, 'utf8', (err) => {
    if (err) {
      console.error('Error writing to file:', err);
      process.exit(1);
    }
    // console.log('File saved successfully.');
  });
});
