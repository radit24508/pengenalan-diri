# server.py
import http.server
import socketserver
import os

PORT = 8000
WEB_DIR = os.path.join(os.path.dirname(__file__), "site")

class MyHandler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=WEB_DIR, **kwargs)

    def log_message(self, format, *args):
        pass  # biar terminal nggak rame log

with socketserver.TCPServer(("", PORT), MyHandler) as httpd:
    print(f"Website berjalan di http://localhost:{PORT}")
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\nServer dihentikan.")
        httpd.server_close()
