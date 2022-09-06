#!/usr/bin/node
const proc = require('process');
const args = proc.argv;
if (Number(args[2]) !== NaN) {
  console.log(`My number: ${args[2]}`);
} else {
  console.log('Not a number');
}
