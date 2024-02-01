# Latest Stories Scraper and API

## Overview
This project consists of two Python scripts:
1. `latestStories.py`: A script to scrape the latest stories from the Time website.
2. `latestStoriesAPI.py`: An HTTP server script that exposes an API endpoint to retrieve the latest stories scraped from the Time website.

## Requirements
- Python 3.x
- `urllib.request` module (for web scraping)
- `re` module (for regular expressions)
- `http.server` module (for creating a simple HTTP server)

## Usage:

### `latestStoriesAPI.py`
This script sets up an HTTP server and exposes an API endpoint (`/getTimeStories`) to retrieve the latest stories scraped from the Time website.

### API Endpoint
The API endpoint can be accessed at `http://localhost:6464/getTimeStories`.

### Example:
```bash
curl http://localhost:6464/getTimeStories

