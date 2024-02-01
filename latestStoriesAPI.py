import re
import json
import http.server
import urllib.request

class MyHandler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/getTimeStories':
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
                    
                    self.send_response(200)
                    self.send_header('Content-type', 'application/json')
                    self.end_headers()
                    self.wfile.write(json.dumps(latest_stories).encode())
                else:
                    self.send_error(500, "Latest stories section not found")
            except Exception as e:
                self.send_error(500, f"Failed to retrieve Time.com content: {e}")
        else:
            self.send_error(404, "Not Found")

def main():
    try:
        server_address = ('', 6464)
        httpd = http.server.HTTPServer(server_address, MyHandler)
        print(f'Server is running on http://localhost:{server_address[1]}')
        httpd.serve_forever()
    except KeyboardInterrupt:
        print('^C received, shutting down the server')
        httpd.socket.close()

if __name__ == '__main__':
    main()
