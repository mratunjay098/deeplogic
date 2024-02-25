# Latest Stories Scraper and API

## Overview
This project consists of two Python scripts and one JavaScript code:
1. `latestStories.py`: A script to scrape the latest stories from the Time website.
2. `latestStoriesAPI.py`: An HTTP server script that exposes an API endpoint to retrieve the latest stories scraped from the Time website.
3. `latestStoriesAPI.js`: An HTTP server script written in JavaScript that exposes an API endpoint to retrieve the latest stories scraped from the Time website.

## Requirements
- For Python scripts:
  - Python 3.x
  - `urllib.request` module (for web scraping)
  - `re` module (for regular expressions)
  - `http.server` module (for creating a simple HTTP server)
  
- For JavaScript script:
  - Node.js
  - `http` module (for creating an HTTP server)
  - `https` module (for making HTTPS requests)
## Usage:

### `latestStoriesAPI.py` and `latestStoriesAPI.js`
The scripts set up an HTTP server and expose an API endpoint (`/getTimeStories`) to retrieve the latest stories scraped from the Time website.

### API Endpoint
The API endpoint can be accessed at `http://localhost:6464/getTimeStories` and `http://localhost:5000/getTimeStories`.

### Example:
```bash
curl http://localhost:6464/getTimeStories
curl http://localhost:5000/getTimeStories

