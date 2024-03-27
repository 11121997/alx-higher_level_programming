#!/usr/bin/node
// script that computes the number of tasks completed by user id

const request = require('request');
const url = process.argv[2];

request(url, function (error, resopnse, body) {
  if (error) {
    console.log(error);
  } else {
    const completedTasks = {};
    const todos = JSON.parse(body);
    for (const doit of todos) {
      if (doit.completed) {
        if (doit.userId in completedTasks) {
          completedTasks[doit.userId] += 1;
        } else {
          completedTasks[doit.userId] = 1;
        }
      }
    }
    console.log(completedTasks);
  }
});
