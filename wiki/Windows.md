<img height="100px" src="https://user-images.githubusercontent.com/28403617/172732896-97a2e867-7e5a-473d-afd4-c00a0378b7ac.svg#gh-light-mode-only" />
<img height="100px" src="https://user-images.githubusercontent.com/28403617/172732894-5a754b66-c657-4830-8a88-6f7d6b0956da.svg#gh-dark-mode-only" />

---

- [DMP File](#dmp-file)
- [Exfiltration](#exfiltration)
- [Kerberos](#kerberos)
- [MSRPC](#msrpc)
- [Ldap](#ldap)
- [Samba](#samba)
- [Virus](#virus)
- [WinRM](#winrm)

## Samba
*Port: 445*

### List Directories
```bash
smbclient  --no-pass -L //ip//
smbclient -U user -L //ip//
```

### Connect
```bash
smbclient "\\\\DOMAIN\\SHARENAME" --no-pass
smbclient  "\\\\DOMAIN\\SHARENAME" -u USER -p PASSWORD
```

### SmbMap
```bash
smbmap -H ip -u anonymous
smbmap -u user -p pass -H ip
```

### Bruteforce
```bash
crackmapexec smb ip -u users.txt -p password.txt
```

## MSRPC
*Port: 135*

### Connect
```bash
rpcclient ip -U user -L -h
```

### Source
- [Different Outils](https://www.hackingarticles.in/impacket-guide-smb-msrpc/)

## WinRM
*Port: 5985*

### Connect
```bash
evil-winrm -i ip -u user -p password
```

## DMP File
### Extract
```bash
Foremost file.dmp
```

## Kerberos
*Port: 88*

Kerberos is an authentication protocol that is used to verify the identity of a user or host.

### Bruteforce User
```bash
kerbrute userenum -d domain --dc ip user.txt
```

### Get user ticket
Checking if Kerberos pre-authentication has been disabled for accounts
```
GetNPUsers.py -usersfile user.txt -no-pass -format hashcat -dc-ip ip domain
```

- [Kerberos cheatsheet](https://gist.github.com/TarlogicSecurity/2f221924fef8c14a1d8e29f3cb5c5c4a)

## Ldap
*Port: 389, 636*

### Nmap
```
nmap -n -sV --script "ldap* and not brute" -p 389 <DC IP>
```

## Exfiltration
### Certificate
```cmd
certutil -encode payload.dll payload.b64
certutil -decode payload.b64 payload.dll
```

## Virus
### Cobalt Strike
- [Cobalt Strike: Using Known Private Keys To Decrypt Traffic – Part 1](https://blog.nviso.eu/2021/10/21/cobalt-strike-using-known-private-keys-to-decrypt-traffic-part-1/)
- [Cobalt Strike: Using Known Private Keys To Decrypt Traffic – Part 2](https://blog.nviso.eu/2021/10/27/cobalt-strike-using-known-private-keys-to-decrypt-traffic-part-2/)
- [Cobalt Strike: Using Process Memory To Decrypt Traffic – Part 3](https://blog.nviso.eu/2021/11/03/cobalt-strike-using-process-memory-to-decrypt-traffic-part-3/)
