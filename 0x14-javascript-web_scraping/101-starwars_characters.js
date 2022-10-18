#!/usr/bin/node
const req = require('request-promise');
const loadData = async () => {
  try {
    const res = await req.get('https://swapi-api.hbtn.io/api/films/' + process.argv[2]);
    const data = await JSON.parse(res).characters;
    for (const buddy of data) {
      const man = await req.get(buddy);
      const name = await JSON.parse(man).name;
      console.log(name);
    }
  } catch (e) {
    console.log(e);
  }
};
loadData();
