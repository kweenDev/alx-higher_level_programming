# JavaScript Web Scraping Project

## Overview
This project comprises JavaScript scripts for web scraping tasks using Node.js. The scripts leverage various modules and APIs to execute actions like file reading and writing, HTTP requests, and data extraction from web sources.

## Scripts
1. **0-readme.js**: Reads and prints the content of a file in UTF-8 format. Handles errors during reading.
2. **1-writeme.js**: Writes a string to a file in UTF-8 format. Handles errors during writing.
3. **2-statuscode.js**: Displays the status code of a GET request to a specified URL using the request module.
4. **3-starwars_title.js**: Prints the title of a Star Wars movie based on the episode number using the Star wars API.
5. **4-starwars_count.js**: Prints the number of movies where the character "Wedge Antilles" is present using the Star wars API.
6. **5-request_store.js**: Gets the contents of a webpage and stores it in a file in UTF-8 format using the request module.
7. **6-completed_tasks.js**: Computes the number of tasks completed by user ID from a JSON API.
8. **100-starwars_characters.js**: Prints all characters of a Star Wars movie based on the movie ID using the Star wars API.
9. **101-starwars_characters.js**: Prints all characters of a Star Wars movie in the order specified by the `/films/` response using the Star wars API.

## Installation and Usage
1. Install Node.js version 14:
```bash
$ curl -sL https://deb.nodesource.com/setup_14.x | sudo -E bash -
$ sudo apt-get install -y nodejs
```
2. Install the semi-standard style:
```bash
$ sudo npm install semistandard --global
```
3. Install the request module:
```bash
$ sudo npm install request --global
```
4. Set the NODE_PATH environment variable:
```bash
$ export NODE_PATH=/usr/lib/node_modules
```

To run a script, use the following format:
```bash
$ ./script_name.js [arguments]
```

For example, to run `0-readme.js`:
```bash
$ ./0-readme.js path/to/file
```

## Credits
- JavaScript resources:
  - Working with JSON data
  - The workflow of accessing attributes of a JSON object by Jimmy Tran
  - [Modern JS Documentation](https://developer.mozilla.org/en-US/docs/Web/JavaScript)
- Star wars API provided by [Star wars API](https://swapi-api.alx-tools.com/api/)
- JSONPlaceholder API provided by [JSONPlaceholder](https://jsonplaceholder.typicode.com/)

## Author
Refiloe Radebe (_kweenDev_)
