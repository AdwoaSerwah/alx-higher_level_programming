#!/usr/bin/node
const request = require('request');

// Check for the correct number of arguments
if (process.argv.length !== 3) {
  console.error('Usage: ./101-starwars_characters.js <Movie_ID>');
  process.exit(1);
}

// Get the Movie ID from command-line argument
const movieId = process.argv[2];
const apiUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}/`;

// Function to fetch character data
const fetchCharacter = (url, callback) => {
  request(url, (error, response, body) => {
    if (error) {
      console.error('Error fetching the character:', error);
      return;
    }
    try {
      const character = JSON.parse(body);
      callback(character.name);
    } catch (err) {
      console.error('Error parsing JSON:', err);
    }
  });
};

// Make the HTTP request to get the movie details
request(apiUrl, (error, response, body) => {
  if (error) {
    console.error('Error fetching the movie data:', error);
    process.exit(1);
  }

  try {
    const movieData = JSON.parse(body);
    const characterUrls = movieData.characters;

    // Fetch and print all character names
    characterUrls.forEach((url, index) => {
      fetchCharacter(url, (name) => {
        console.log(name);
      });
    });
  } catch (err) {
    console.error('Error parsing movie JSON:', err);
    process.exit(1);
  }
});
