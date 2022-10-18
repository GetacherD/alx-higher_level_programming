#!/usr/bin/node
const req = require('sync-request');

const res = req('GET', 'https://swapi-api.hbtn.io/api/films/' + process.argv[2]);
const data = JSON.parse(res.getBody()).characters;
for (const ch of data) {
  console.log(JSON.parse(req('GET', ch).getBody()).name);
}
