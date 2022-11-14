#!/usr/bin/python3

import requests
import sys

s = requests.session()
# s.proxies = {
#   "http": "localhost:8080",
#   "https": "localhost:8080",
# }

# Classic Get
r = s.get('http://example.com')
print(r.text)

# Classic Post
r = s.post('http://example.com/submit',
    headers={
        'Content-type': 'application/json',
        # 'Content-type': 'application/x-www-form-urlencoded',
        # 'Content-type': 'application/xml',
        # 'Content-type': 'raw',
    },
    data={'user': 'guest'},
    # auth=('username', 'password')
)
print(r.status_code, r.url)

# File POST
files = { 'fileToUpload': ('lel.jpg', open('lel.jpg', 'rb').read()) }
r = s.post('http://example.com/upload.php',
    files=files,
)
print(r.text)