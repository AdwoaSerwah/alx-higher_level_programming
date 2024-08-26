#!/usr/bin/node
const request = require('request');
const { promisify } = require('util');

const requestAsync = promisify(request);

// Function to fetch a character's name
const fetchCharacterName = async (url) => {
  try {
    const { body } = await requestAsync(url);
    const character = JSON.parse(body);
    return character.name;
  } catch (error) {
    console.error('Error fetching character data:', error);
    return null;
  }
};

// Function to fetch movie data and print characters
const fetchMovieData = async (movieId) => {
  const apiUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}/`;

  try {
    const { body } = await requestAsync(apiUrl);
    const movieData = JSON.parse(body);
    const characterUrls = movieData.characters;

    if (characterUrls && characterUrls.length > 0) {
      // Print the characters part of the API response
      // console.log('Characters URLs:');
      // console.log(characterUrls);

      // console.log('\nCharacter Names:');
      // Fetch and print characters in the same order as the URLs
      for (const url of characterUrls) {
        const name = await fetchCharacterName(url);
        if (name) {
          console.log(name);
        }
      }
    } else {
      console.log('No characters found');
    }
  } catch (error) {
    console.error('Error fetching movie data:', error);
    process.exit(1);
  }
};

// Check for the correct number of arguments
if (process.argv.length !== 3) {
  console.error('Usage: ./101-starwars_characters.js <Movie_ID>');
  process.exit(1);
}

// Get the Movie ID from command-line argument
const movieId = process.argv[2];
fetchMovieData(movieId);
