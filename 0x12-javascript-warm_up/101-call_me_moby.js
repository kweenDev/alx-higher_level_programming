#!/usr/bin/node
// Define the callMeMoby function and export it
exports.callMeMoby = function (x, theFunction) {
  for (let i = 0; i < x; i++) {
    theFunction();
  }
};
