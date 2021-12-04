#!/usr/bin/python3

import requests
import sys

s = requests.session()
# s.proxies = {
#   "http": "localhost:8080",
#   "https": "localhost:8080",
# }

r = s.get('http://example.com')
print(r.text)
r = s.post('http://example.com/submit',
    headers={
        'Content-type': 'raw',
    },
    data={'user': 'guest'},
    # auth=('username', 'password')
)
print(r.status_code, r.url)