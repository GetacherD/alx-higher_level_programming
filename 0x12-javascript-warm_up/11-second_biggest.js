#!/usr/bin/node
const proc = require('process');
const args = proc.argv;
let i = 2;
let firstMax = 0;
let secondMax = 0;
if (isNaN(Number(args[2]))) {
  console.log(0);
} else if (isNaN(Number(args[3]))) {
  console.log(0);
} else {
  firstMax = Number(args[2]);
  secondMax = 0;
  while (!isNaN(Number(args[i]))) {
    if (Number(args[i]) > firstMax) {
      secondMax = firstMax;
      firstMax = Number(args[i]);
    } else if (Number(args[i]) > secondMax) {
      secondMax = Number(args[i]);
    }
    i++;
  }
  console.log(secondMax);
}
