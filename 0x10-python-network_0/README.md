# 0x10. Python - Network #0

## Description

This project focuses on learning about network basics, HTTP, URLs, cURL, HTTP headers, HTTP request methods, HTTP response status codes, and more.

## Project Files

- **0-body_size.sh:** Bash script that takes in a URL, sends a request to that URL, and displays the size of the body of the response in bytes using curl.

- **1-body.sh:** Bash script that takes in a URL, sends a GET request to the URL, and displays the body of the response if the status code is 200 using curl.

- **2-delete.sh:** Bash script that sends a DELETE request to the URL passed as the first argument and displays the body of the response using curl.

- **3-methods.sh:** Bash script that takes in a URL and displays all HTTP methods the server will accept using curl.

- **4-header.sh:** Bash script that takes in a URL as an argument, sends a GET request to the URL with a header variable X-School-User-Id set to 98, and displays the body of the response using curl.

- **5-post_params.sh:** Bash script that takes in a URL, sends a POST request to the passed URL with variables email set to test@gmail.com and subject set to I will always be here for PLD, and displays the body of the response using curl.

## Requirements

- All scripts are tested on Ubuntu 20.04 LTS.
- Bash scripts are exactly 3 lines long.
- Files end with a new line.
- All files are executable.
- Python files use pycodestyle (version 2.8.*) for code style checking.
- All modules, classes, and functions are documented.

## Usage

To run the scripts, use the following format:

```bash
./script_name.sh URL
```
Replace script_name.sh with the name of the script you want to run and URL with the desired URL.

Author
Author: _kweenDev_ (Refiloe Radebe)
Date: 2024-04-15
