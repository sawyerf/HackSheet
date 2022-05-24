# 🐍 Python

- [Base64](#base64)
- [Execute Command](#execute-command)
- [Pwn](#pwn)
- [Requests](#requests)

## Requests
```python
import requests
```

### GET
```python
r = requests.get('http://example.com')
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

## Base64
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

## Socket
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
# Receive
sock.recv(1024) # b'Random content'
# Send
sock.send(b'Random content')
# Close
sock.close()
```

## Execute Command
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

## Pwn
- [Example script](https://github.com/sawyerf/HackSheet/blob/main/scripts/pwn-connect.py)