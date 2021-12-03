import sys
from http.server import HTTPServer, BaseHTTPRequestHandler

class Redirect(BaseHTTPRequestHandler):
   def do_GET(self):
       self.send_response(302)
       self.send_header('Location', sys.argv[1])
       self.end_headers()

if len(sys.argv) - 1 != 2:
    print("""
Usage: {} <url>
    """.format(sys.argv[0]))
    sys.exit()

HTTPServer(("", 80, Redirect).serve_forever()