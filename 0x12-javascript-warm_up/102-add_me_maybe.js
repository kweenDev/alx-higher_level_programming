#!/usr/bin/node
// Define the addMeMaybe function and export it
exports.addMeMaybe = function(number, theFunction) {
	theFunction(number + 1);
};
