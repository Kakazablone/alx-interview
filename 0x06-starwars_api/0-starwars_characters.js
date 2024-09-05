#!/usr/bin/node
const argv = process.argv;
const request = require('request');

const urlFilm = 'https://swapi-api.alx-tools.com/api/films/';
const urlMovie = `${urlFilm}${argv[2]}/`;

function fetchCharacter (url, callback) {
  request(url, function (error, response, body) {
    if (!error && response.statusCode === 200) {
      const character = JSON.parse(body);
      console.log(character.name);
      callback();
    } else {
      console.error('Error fetching character:', error);
    }
  });
}

function fetchMovie () {
  request(urlMovie, function (error, response, body) {
    if (!error && response.statusCode === 200) {
      const movie = JSON.parse(body);
      const characters = movie.characters;

      let count = 0;
      function fetchNextCharacter () {
        if (count < characters.length) {
          fetchCharacter(characters[count], function () {
            count++;
            fetchNextCharacter();
          });
        }
      }

      fetchNextCharacter();
    } else {
      console.error('Error fetching movie:', error);
    }
  });
}

// Start fetching movie data
fetchMovie();
