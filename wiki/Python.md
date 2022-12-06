<picture>
    <source height="100px" srcset="https://user-images.githubusercontent.com/22857002/173634298-2954a444-d38b-4b9f-a729-70b339a6c6b6.svg#gh-dark-mode-only" media="(prefers-color-scheme: dark)">
    <img height="100px" src="https://user-images.githubusercontent.com/28403617/172731520-180b308c-a207-4a2f-95f5-0c5aac40881e.svg#gh-light-mode-only">
</picture>

---

- [Base64](#base64)
- [Execute Command](#execute-command)
- [Hash](#hash)
- [Pwn](#pwn)
- [Requests](#requests)
- [Server](#server)
- [Socket](#socket)
- [Thread](#thread)
- [Urlencode](#urlencode)

# Requests
```python
import requests
```

### GET
```python
r = requests.get('http://example.com')
```

### Session
```python
# Replace requests by `s` in your future requests to use session.
s = requests.session()
```

### Proxies
```python
s.proxies = {
  "http": "localhost:8080",
  "https": "localhost:8080",
}
```

### POST
```python
# Classic Post
r = requests.post('http://example.com/submit',
    headers={
        'Content-type': 'application/x-www-form-urlencoded',
    },
    data={'user': 'guest'},
    verify=False # Check Certificate
)
```

- [Example Script](/scripts/requests-classic.py)

### Response Objects
```python
r.url
r.status_code
r.headers
r.cookies
r.raw
r.content # Byte
r.text    # String
r.request
```
- [Docs](https://requests.readthedocs.io/en/latest/user/advanced/#request-and-response-objects)

### Example
- [Example script](https://github.com/sawyerf/HackSheet/blob/main/scripts/requests-classic.py)

# Server
### Handler
```python
from http.server import HTTPServer, BaseHTTPRequestHandler

class httpHandler(BaseHTTPRequestHandler):
	def do_GET(self):
		self.send_response(200)
		self.end_headers()
		self.wfile.write(b'Hello World')

	def do_POST():
		pass

httpd = HTTPServer(('0.0.0.0', 8000), httpHandler)
httpd.serve_forever()
```

- [http.server doc](https://docs.python.org/3/library/http.server.html#http.server.BaseHTTPRequestHandler)

# Base64
```python
import base64
```

### Decode
```python
encodedStr = "VGVzdCBSYW5kb20gU3RyaW5n"
text = base64.b64decode(encodedStr).decode() # 'Test Random String'
```

### Encode
```python
data = "Test Random String"
encodedBytes = base64.b64encode(data.encode()).decode() # 'VGVzdCBSYW5kb20gU3RyaW5n'
```

# Urlencode
```python
import urllib.parse
```

### Decode
```python
urllib.parse.quote('/Tést Rä') # '/T%C3%A9st%20R%C3%A4'
urllib.parse.quote('/', safe='') # '%2F'
```

### Encode
```python
urllib.parse.unquote('lol+lol') # 'lol+lol'
urllib.parse.unquote_plus('lol+lol') # 'lol lol'
```

- [How to encode URLs in Python](https://www.urldecoder.io/python/)

# Socket
```python
import socket
```

### Server
```python
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
    server.bind(('', 4444))
    server.listen()
    sock, addr = server.accept()
```

### Client
```python
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
    sock.connect(('127.0.0.1', 4444))
```

### Common
```python
# Set Timeout
sock.settimeout(5)
# Receive
sock.recv(1024) # b'Random content'
# Send
sock.send(b'Random content')
# Close
sock.close()
```

# Execute Command
### Os
```python
import os
```
```python
os.system('echo desbarres') # Exit Code
```
```python
os.popen('echo desbarres').read() # 'desbarres'
```

### Subprocess
```python
import subprocess
```
```python
subprocess.call('echo desbarres', shell=True) # Exit Code
```
```python
subprocess.check_output('echo desbarres', shell=True) # b'desbarres'
```

# Thread
```python
from threading import Thread
```
### Run function
```python
thr = Thread(target=func, args=(1,))
thr.start()
thr.join()
```

### Run class
```python
class ExampleClass(Thread):
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)

	def run(self):
		do_stuff

thr = ExampleClass()
thr.start()
```

# Hash
```python
import hashlib
```

### MD5
```python
hashlib.md5(b'password').hexdigest() # '5f4dcc3b5aa765d61d8327deb882cf99'
```

### Sha256
```python
hashlib.sha256(b'password').hexdigest() # '5e884898da28047151d0e56f8dc6292773603d0d6aabbdd62a11ef721d1542d8'
```

# Pwn
- [Example script](https://github.com/sawyerf/HackSheet/blob/main/scripts/pwn-connect.py)
- [Shellcode](/wiki/ReverseEngineering.md#shellcode)