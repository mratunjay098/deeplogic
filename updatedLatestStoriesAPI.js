const http = require('http');
const https = require('https');

function extractStories(htmlContent) {
  const stories = [];
  let currentIndex = htmlContent.indexOf('<li class="latest-stories__item">');

  while (currentIndex !== -1) {
    const startIndex = htmlContent.indexOf('<a', currentIndex);
    const endIndex = htmlContent.indexOf('</a>', startIndex);

    if (startIndex !== -1 && endIndex !== -1) {
      const hrefStartIndex = htmlContent.indexOf('href="', startIndex) + 'href="'.length;
      const hrefEndIndex = htmlContent.indexOf('"', hrefStartIndex);
      let link = htmlContent.substring(hrefStartIndex, hrefEndIndex);

      link = link.replace(/\\+/g, '');

      const titleStartIndex = htmlContent.indexOf('>', htmlContent.indexOf('<h3', startIndex)) + 1;
      const titleEndIndex = htmlContent.indexOf('</h3>', titleStartIndex);
      const title = htmlContent.substring(titleStartIndex, titleEndIndex).trim();

      stories.push({ title, link });
    }

    currentIndex = htmlContent.indexOf('<li class="latest-stories__item">', currentIndex + 1);
  }

  return stories;
}

function fetchHTML(url, callback) {
  https.get(url, (response) => {
    let data = '';

    response.on('data', (chunk) => {
      data += chunk;
    });

    response.on('end', () => {
      callback(null, data);
    });
  }).on('error', (error) => {
    callback(error, null);
  });
}

const server = http.createServer((req, res) => {
  if (req.url === '/getTimeStories' && req.method === 'GET') {
    const targetURL = 'https://time.com/';

    fetchHTML(targetURL, (error, htmlContent) => {
      if (error) {
        res.writeHead(500, { 'Content-Type': 'application/json' });
        res.end(JSON.stringify({ error: 'Internal Server Error' }));
      } else {
        const stories = extractStories(htmlContent);
        res.writeHead(200, { 'Content-Type': 'application/json' });
        res.end(JSON.stringify(stories));
      }
    });
  } else {
    res.writeHead(404, { 'Content-Type': 'text/plain' });
    res.end('Not Found');
  }
});

const port = 5000;
server.listen(port, () => {
  console.log(`Server is running on http://localhost:${port}`);
  console.log(`You can get the Latest Stories using the endpoint: /getTimeStories`);
});
