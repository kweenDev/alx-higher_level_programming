#!/usr/bin/node
const myObject = {
	type: 'object',
	value: 12,
	// Define the incr function inside the myObject object
	incr: function() {
		this.value++;
	}
};

console.log(myObject);

// Call the incr function to increment the value
myObject.incr();
console.log(myObject);

myObject.incr();
console.log(myObject);

myObject.incr();
console.log(myObject);
