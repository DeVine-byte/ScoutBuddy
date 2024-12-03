# ScoutBuddy

ScoutBuddy is a simple Python-based tool designed for web security analysis. It provides three main features:

1. **Header Analysis**: Analyzes HTTP headers for security configurations.
2. **Form Extraction**: Extracts and displays all `<form>` elements from a web page.
3. **Web Crawling**: Fetches and lists all the links on a target webpage.

---

## Introduction

ScoutBuddy helps in conducting a quick analysis of a website's security posture by examining HTTP headers, extracting form fields for validation, and crawling links from the given webpage. It is designed for web security enthusiasts and penetration testers.

---

## Features

- **Header Analysis**: Checks for important security headers such as `X-Frame-Options`, `Content-Security-Policy`, and `X-XSS-Protection`.
- **Form Extraction**: Extracts all `<form>` elements from a webpage for analysis and testing.
- **Web Crawling**: Lists all links (`<a>` tags) found on a given page, useful for mapping out a website.

---

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/DeVine-byte//ScoutBuddy.git
2. cd ScoutBuddy
3. ```bash
   pip install -r requirements.txt

## Usage
python scout.py

## License
This project is licensed under the Apache License 2.0. See the LICENSE file for details.
