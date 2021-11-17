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

## WinRM
*Port: 5985*

### Connect
```
evil-winrm -i ip -u user -p password
```
