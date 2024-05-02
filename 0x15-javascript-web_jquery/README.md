# 0x15. JavaScript - Web jQuery
### 0x15-javascript-web_jquery

## Description
This project focuses on JavaScript front-end development using JQuery. It includes various tasks that involve DOM manipulation, event handling, and API integration.

## Concepts Covered
- JavaScript in the browser
- Dealing with data statically versus dynamically
- JQuery for DOM manipulation
- Handling API requests

## Learning Objectives
By completing this project, you will be able to:
- Explain the ease of front-end programming with JQuery
- Select HTML elements using JavaScript and JQuery
- Understand the differences between ID, class, and tag name selectors
- Modify HTML element styles and content dynamically
- Make GET and POST requests using JQuery Ajax
- Handle DOM and user events effectively

## Requirements
- Editors: vi, vim, emacs
- Chrome (version 57.0) compatibility
- Files should end with a new line
- Semistandard compliant code with the flag `--global $: semistandard *.js --global $`
- Use JQuery version 3.x
- Do not use `var`
- HTML should not reload for each action
- Import JQuery:
  ```html
  <head>
      <script src="https://code.jquery.com/jquery-3.2.1.min.js"></script>
  </head>
  ```

## Tasks
##### Task 0: No JQuery
- Write a JavaScript script that updates the text color of the `<header>` element to red (#FF0000):
	- Use document.querySelector to select the HTML tag.
	- Do not use the JQuery API.

##### Task 1: With JQuery
- Write a JavaScript script that updates the text color of the `<header>` element to red (#FF0000):
	- Use the JQuery API.
	- Do not use `document.querySelector` to select the HTML tag.

##### Task 2: Click and turn red
- Write a JavaScript script that updates the text color of the `<header>` element to red (#FF0000) when the user clicks on the tag DIV#red_header:
	- Use the JQuery API.
	- Do not use `document.querySelector` to select the HTML tag.

##### Task 3: Add .red class
- Write a JavaScript script that adds the class red to the `<header>` element when the user clicks on the tag DIV#red_header:
	- Use the JQuery API.
	- Do not use `document.querySelector` to select the HTML tag.

##### Task 4: Toggle classes
- Write a JavaScript script that toggles the class of the `<header>` element when the user clicks on the tag DIV#toggle_header:
	- The `<header>` element must always have one class: red or green, never both at the same time and never empty.
	- If the current class is red, when the user clicks on DIV#toggle_header, the class must be updated to green; and vice versa.
	- Use the JQuery API.
	- Do not use `document.querySelector` to select the HTML tag.

##### Task 5: List of elements
- Write a JavaScript script that adds a `<li>` element to a list when the user clicks on the tag DIV#add_item:
	- The new element must be: `<li>Item</li>`.
	- The new element must be added to UL.my_list.
	- Use the JQuery API.
	- Do not use `document.querySelector` to select the HTML tag.

##### Task 6: Change the text
- Write a JavaScript script that updates the text of the `<header>` element to "New Header!!!" when the user clicks on DIV#update_header:
	- Use the JQuery API.
	- Do not use `document.querySelector` to select the HTML tag.

##### Task 7: Star wars character
- Write a JavaScript script that fetches the character name from this URL: https://swapi-api.alx-tools.com/api/people/5/?format=json
	- The name must be displayed in the HTML tag DIV#character.
	- Use the JQuery API.
	- Do not use `document.querySelector` to select the HTML tag.

##### Task 8: Star Wars movies
- Write a JavaScript script that fetches and lists the title for all movies by using this URL: https://swapi-api.alx-tools.com/api/films/?format=json
	- All movie titles must be listed in the HTML tag UL#list_movies.
	- Use the JQuery API.
	- Do not use `document.querySelector` to select the HTML tag.

##### Task 9: Say Hello!
- Write a JavaScript script that fetches from https://hellosalut.stefanbohacek.dev/?lang=fr and displays the value of hello from that fetch in the HTML tag DIV#hello.
	- The translation of “hello” must be displayed in the HTML tag DIV#hello.
	- Use the JQuery API.
	- Do not use `document.querySelector` to select the HTML tag.

##### Task 10: No jQuery - document loaded
- Write a JavaScript script that updates the text color of the `<header>` element to red (#FF0000):
	- Use `document.querySelector` to select the HTML tag.
	- Do not use the JQuery API.

##### Task 11: List, add, remove
- Write a JavaScript script that adds, removes, and clears LI elements from a list when the user clicks:
	- The new element must be: `<li>Item</li>`.
	- The new element must be added to UL.my_list.
	- When the user clicks on DIV#add_item, a new element is added to the list.
	- When the user clicks on DIV#remove_item, the last element is removed from the list.
	- When the user clicks on DIV#clear_list, all elements of the list are removed.
	- Use the JQuery API.
	- Do not use `document.querySelector` to select the HTML tag.

##### Task 12: Say hello to everybody!
- Write a JavaScript script that fetches and prints how to say “Hello” depending on the language:
	- Use the API service: https://www.fourtonfish.com/hellosalut/hello/
	- The language code will be the value entered in the tag INPUT#language_code (ex: es, fr, en etc.)
	- The translation must be fetched when the user clicks on INPUT#btn_translate.
	- The translation of “Hello” must be displayed in the HTML tag DIV#hello.
	- Use the JQuery API.
	- Do not use `document.querySelector` to select the HTML tag.

##### Task 13: And press ENTER
- Write a JavaScript script that fetches and prints how to say “Hello” depending on the language:
	- Use the API service: https://www.fourtonfish.com/hellosalut/hello/
- The language code will be the value entered in the tag INPUT#language_code (ex: es, fr, en etc.)
	- The translation must be fetched when the user clicks on INPUT#btn_translate OR presses ENTER when the focus is on INPUT#language_code.
	- The translation of “Hello” must be displayed in the HTML tag DIV#hello.
	- Use the JQuery API.
	- Do not use `document.querySelector` to select the HTML tag.

## Repository Structure
0x15-javascript-web_jquery/
README.md: Project description and instructions.
0-script.js: Script for task 0.
1-script.js: Script for task 1.
2-script.js: Script for task 2.
3-script.js: Script for task 3.
4-script.js: Script for task 4.
5-script.js: Script for task 5.
6-script.js: Script for task 6.
7-script.js: Script for task 7.
8-script.js: Script for task 8.
9-script.js: Script for task 9.
100-script.js: Script for task 10.
101-script.js: Script for task 11.
102-script.js: Script for task 12.
103-script.js: Script for task 13.

## How to Run
1. Clone the repository:
```bash
git clone https://github.com/alx-higher_level_programming/0x15-javascript-web_jquery.git
```
2. Open the HTML files in your browser to test each script.

## Author
Refiloe Radebe (_kweenDev_)
