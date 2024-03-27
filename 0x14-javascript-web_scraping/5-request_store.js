#!/usr/bin/node
// script that gets the contents of a webpage and stores it in a file

const request = require('request');
const fs = require('fs');

request(process.argv[2], function (err, response, body) {
  if (err) {
    console.log(err);
  } else {
    fs.writefile(process.argv[3], body, 'utf-8', function (err) {
      if (err) {
        console.log(err);
      }
    });
  }
});
