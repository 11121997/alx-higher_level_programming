#!/usr/bin/node
// script that prints all characters of a Star Wars movie

const request = require('request');
const id = process.argv[2];
const url = 'https://swapi-api.alx-tools.com/api/films/' + id;

function printChars (chars, idx) {
  request(chars[idx], function (err, response, body) {
    if (err) {
      console.log(err);
    } else {
      console.log(JSON.parse(body).name);
      if (idx + 1 < chars.length) {
        printChars(chars, idx + 1);
      }
    }
  });
}

request(url, function (err, response, body) {
  if (err) {
    console.log(err);
  } else {
    const chars = JSON.parse(body).characters;
    printChars(chars, 0);
  }
});
