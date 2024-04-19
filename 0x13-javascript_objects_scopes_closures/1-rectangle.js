#!/usr/bin/node
// 1-rectangle.js

class Rectangle {
  constructor (w, h) {
    this.width = w
    this.height = h
  }
}

module.exports = Rectangle

// Define the class Rectangle usingh the class keyword.
// The constructor method takes two arguments w and h, which represent the width and height of the rectangle.
// Inside the constructor, the instance attricutes width and height are initialized with the values of w and h passed to the constructor.
// Finally, the Rectangle class is exported using module.exports for use in other files.
