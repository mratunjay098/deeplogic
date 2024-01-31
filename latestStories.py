import re
import json
import urllib.request

def get_time_stories():
    try:
        url = "https://time.com"
        response = urllib.request.urlopen(url)
        html_content = response.read().decode("utf-8")
        
        pattern = r'<div class="partial latest-stories"[^>]*>.*?<ul>(.*?)</ul>.*?</div>'
        
        latest_stories_match = re.search(pattern, html_content, re.DOTALL)
        if latest_stories_match:
            latest_stories_html = latest_stories_match.group(1)
            
            item_pattern = r'<li class="latest-stories__item">.*?<a href="(.*?)">.*?<h3 class="latest-stories__item-headline">(.*?)</h3>.*?<time[^>]*>(.*?)</time>.*?</li>'
            
            matches = re.findall(item_pattern, latest_stories_html, re.DOTALL)
            
            latest_stories = [{"title": match[1], "link": "https://time.com" + match[0]} for match in matches[:6]]
            
            return latest_stories
        else:
            print("Latest stories section not found.")
            return []
    except Exception as e:
        print("Failed to retrieve Time.com content:", e)
        return []

if __name__ == "__main__":
    latest_stories = get_time_stories()
    print(json.dumps(latest_stories, indent=4))