from http.server import BaseHTTPRequestHandler, HTTPServer


class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        body = b'<h1>Hello from the Python app!</h1>\n'
        self.send_response(200)
        self.send_header('Content-Type', 'text/html; charset=utf-8')
        self.send_header('Content-Length', str(len(body)))
        self.end_headers()
        self.wfile.write(body)


server = HTTPServer(('0.0.0.0', 5000), Handler)
print('Python app listening on port 5000', flush=True)
server.serve_forever()
