#!/usr/bin/node
// script that computes the number of tasks completed by user id

const request = require('request');
const url = process.argv[2];

request(url, function (err, response, body) {
  if (err) {
    console.log(err);
  } else {
    const doits = JSON.parse(body);
    const completedTasks = {};

    for (const doit of doits) {
      if (doit.completed) {
        if (doit.userID in completedTasks) {
          completedTasks[doit.userId]++;
        } else {
          completedTasks[doit.userId] = 1;
        }
      }
    }
    console.log(completedTasks);
  }
});
