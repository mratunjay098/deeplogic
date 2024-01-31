# time.com Latest Stories Scraper

This Python script fetches the latest stories from the time.com website and extracts their titles and links.

## Requirements

- Python 3.9.x
- `urllib.request` module (included in Python standard library)
- `re` module (included in Python standard library)
- `json` module (included in Python standard library)

## Usage

1. Clone the repository or download the script `latestStories.py`.
2. Run the script using Python.


## Functionality

- The script sends a GET request to the time.com website to fetch the HTML content.
- It then extracts the latest stories section from the HTML using regular expressions.
- For each story, it extracts the title and link.
- The script returns a JSON object containing the latest 6 stories with their titles and links.

## Sample Output

The output for date 31 Jan 2024 will be a JSON object with the following structure:

```json
[
    {
        "title": "Climate Change Behind Africa Cholera Surge",
        "link": "https://time.com/6590560/climate-change-africa-cholera-surge/"
    },
    {
        "title": "The Best New TV Shows of January 2024",
        "link": "https://time.com/6589092/best-tv-shows-january-2024/"
    },
    {
        "title": "UMG to Remove Music From TikTok",
        "link": "https://time.com/6590486/tiktok-music-umg-taylor-swift/"
    },
    {
        "title": "Utah Joins States Regulating Bathroom Access for Transgender People",
        "link": "https://time.com/6590528/utah-joins-states-regulating-bathroom-access-transgender-people/"
    },
    {
        "title": "The Best and Worst Super Bowl LVIII Ads",
        "link": "https://time.com/6590433/super-bowl-2024-adverts-best-worst/"
    },
    {
        "title": "'Feud: Capote vs. the Swans': TV Review",
        "link": "https://time.com/6588110/feud-capote-vs-swans-review/"
    }
] 
