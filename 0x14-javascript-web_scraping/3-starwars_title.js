#!/usr/bin/node

const request = require('request');

// Get the movie ID from the first argument
const movieId = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

// Make a GET request to the Star Wars API
request(url, (error, response, body) => {
  if (error) {
    console.log(error);
  } else {
    const movie = JSON.parse(body);
    console.log(movie.title);
  }
});
