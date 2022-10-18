#!/usr/bin/node
const req = require('request');
req.get('https://swapi-api.hbtn.io/api/films/' + process.argv[2], function (err, resp, body) {
  if (err) {
    console.log(err);
  } else {
    const data = JSON.parse(body).characters;
    print(data, 0);
  }
});
function print (data, index) {
  req.get(data[index], function (err, resp, body) {
    if (err) {
      console.log(err);
    } else {
      console.log(JSON.parse(body).name);
    }
  });
  const len = data.length;
  if (index + 1 < len) {
    print(data, index + 1);
  }
}
