# Windows

- [Samba](#samba)
- [MSRPC](#msrpc)
- [WinRM](#winrm)

## Samba
*Port: 445*

### Connect
```
smbclient -U user -L //ip//
```

## MSRPC
*Port: 135*

### Connect
```
rpcclient ip -U user -L -h
```

### Source
[Different Outils](https://www.hackingarticles.in/impacket-guide-smb-msrpc/)

## WinRM
*Port: 5985*

### Connect
```
evil-winrm -i ip -u user -p password
```
