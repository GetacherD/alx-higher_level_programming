#!/usr/bin/node
const proc = require('process');
const num = Number(proc.argv[2]);
if (num != num || num === undefined) {
  console.log('Not a number');
} else {
  console.log(`My number: ${num}`);
}
