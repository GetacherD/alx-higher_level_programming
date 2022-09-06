#!/usr/bin/node
exports.callMe = function (x, theFunction) {
  let i = 0;
  while (i < Math.floor(Number(x))) {
    theFunction();
    i++;
  }
};
