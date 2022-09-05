#!/usr/bin/node
const proc = require('process');
const process = proc.argv;

if (process.length === 2) {
  console.log('No argument');
} else if (process.length === 3) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
