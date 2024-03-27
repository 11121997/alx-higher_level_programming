#!/usr/bin/node
// script that computes the number of tasks completed by user id

const request = require('request');
const url = process.argv[2];

request(url, function (err, response, body) {
  if (err) {
    console.log(err);
  } else {
    const doit = JSON.parse(body);
    const completedTasks = {};

    for (const doing of doit) {
      if (doing.completed) {
        if (doing.userID in completedTasks) {
          completedTasks[doing.userId] += 1;
        } else {
          completedTasks[doing.userId] = 1;
        }
      }
    }
    console.log(completedTasks);
  }
});
