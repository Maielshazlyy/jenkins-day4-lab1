const http = require('http');

const port = 3000;
const server = http.createServer((_request, response) => {
  response.writeHead(200, { 'Content-Type': 'text/html; charset=utf-8' });
  response.end('<h1>Hello from the Node.js app!</h1>\n');
});

server.listen(port, '0.0.0.0', () => {
  console.log(`Node.js app listening on port ${port}`);
});
