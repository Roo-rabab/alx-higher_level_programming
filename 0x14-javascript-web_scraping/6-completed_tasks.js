#!/usr/bin/node
// script that computes the number of tasks completed by user id

const request = require('request');
const url = process.argv[2];
request.get(url, { json: true }, (error, response, body) => {
  if (error) {
    console.log(error);
    return;
  }
  const taskscompleted = {};
  body.forEach((todo) => {
    if (todo.completed) {
      if (!taskscompleted[todo.userId]) {
        taskscompleted[todo.userId] = 1;
      } else {
        taskscompleted[todo.userId] += 1;
      }
    }
  });
  console.log(taskscompleted);
});
