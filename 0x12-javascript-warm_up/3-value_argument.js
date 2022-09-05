#!/usr/bin/node
const proc = require('process');
const args = proc.argv;
if (args[2] !== undefined) {
  console.log(args[2]);
} else {
  console.log('No argument');
}
