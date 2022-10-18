#!/usr/bin/node

const request = require('request');
function doRequest (url) {
  return new Promise(function (resolve, reject) {
    request(url, function (error, res, body) {
      if (!error && res.statusCode === 200) {
        resolve(JSON.parse(body));
      } else {
        reject(error);
      }
    });
  });
}

async function main () {
  try {
    const response = await doRequest('https://swapi-api.hbtn.io/api/films/' + process.argv[2]);
    for (const ur of response.characters) {
      const resp = await doRequest(ur);
      console.log(resp.name);
    }
  } catch (error) {
    console.error(error);
  }
}

main();
