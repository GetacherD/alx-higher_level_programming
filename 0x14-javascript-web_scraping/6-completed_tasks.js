#!/usr/bin/node
const req = require('request');

req.get(process.argv[2], { json: true }, function (err, resp, body) {
  if (err) {
    console.error(err);
  } else {
    const res = {};
    for (const todo of body) {
      if (res[todo.userId] === undefined) {
        res[todo.userId] = 0;
      } else {
        if (todo.completed === true) {
          res[todo.userId] = res[todo.userId] + 1;
        }
      }
    }
    console.log(res);
  }
});
