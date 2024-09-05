#!/usr/bin/node
const argv = process.argv;
const axios = require('axios');

const urlFilm = 'https://swapi-api.hbtn.io/api/films/';
const urlMovie = `${urlFilm}${argv[2]}/`;

async function fetchCharacter (url) {
  try {
    const response = await axios.get(url);
    console.log(response.data.name);
  } catch (error) {
    console.error('Error fetching character:', error);
  }
}

async function fetchMovie () {
  try {
    const response = await axios.get(urlMovie);
    const characters = response.data.characters;

    // Fetch each character sequentially
    for (let i = 0; i < characters.length; i++) {
      await fetchCharacter(characters[i]);
    }
  } catch (error) {
    console.error('Error fetching movie:', error);
  }
}

// Start fetching movie data
fetchMovie();
