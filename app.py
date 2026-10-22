import json
import os
from http.server import BaseHTTPRequestHandler, HTTPServer


class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/health':
            body = {'status': 'ok'}
        elif self.path == '/config':
            body = {'service': 'ShipDesk', 'mode': os.environ.get('APP_MODE', 'development'),
                    'version': '1.1.0'}
        else:
            self.send_error(404)
            return
        data = (json.dumps(body) + '\n').encode()
        self.send_response(200)
        self.send_header('Content-Type', 'application/json')
        self.send_header('Content-Length', str(len(data)))
        self.end_headers()
        self.wfile.write(data)


if __name__ == '__main__':
    print('ShipDesk listening on 0.0.0.0:8000', flush=True)
    HTTPServer(('0.0.0.0', 8000), Handler).serve_forever()
