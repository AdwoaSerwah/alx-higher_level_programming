#!/usr/bin/node
const request = require('request');

// Check for the correct number of arguments
if (process.argv.length !== 3) {
  console.error('Usage: ./100-starwars_characters.js <Movie_ID>');
  process.exit(1);
}

// Get the Movie ID from command-line argument
const movieId = process.argv[2];
const apiUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}/`;

// Make the HTTP request
request(apiUrl, (error, response, body) => {
  if (error) {
    console.error('Error fetching the URL:', error);
    process.exit(1);
  }

  try {
    // Parse the JSON response
    const movieData = JSON.parse(body);

    // Get the list of character URLs
    const characterUrls = movieData.characters;

    // Helper function to fetch character names
    const fetchCharacterNames = (urls, index) => {
      if (index >= urls.length) {
        return;
      }

      request(urls[index], (err, res, charBody) => {
        if (err) {
          console.error('Error fetching character:', err);
        } else {
          try {
            const character = JSON.parse(charBody);
            console.log(character.name);
          } catch (err) {
            console.error('Error parsing character JSON:', err);
          }
        }
        fetchCharacterNames(urls, index + 1);
      });
    };

    // Start fetching character names
    fetchCharacterNames(characterUrls, 0);
  } catch (err) {
    console.error('Error parsing JSON:', err);
    process.exit(1);
  }
});
