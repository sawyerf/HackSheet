# 🪟 Windows

- [DMP File](#dmp-file)
- [Exfiltration](#exfiltration)
- [MSRPC](#msrpc)
- [Samba](#samba)
- [Virus](#virus)
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
- [Different Outils](https://www.hackingarticles.in/impacket-guide-smb-msrpc/)

## WinRM
*Port: 5985*

### Connect
```
evil-winrm -i ip -u user -p password
```

## DMP File
### Extract
```
Foremost file.dmp
```

## Exfiltration
### Certificate
```
certutil -encode payload.dll payload.b64
certutil -decode payload.b64 payload.dll
```

## Virus
### Cobalt Strike
- [Cobalt Strike: Using Known Private Keys To Decrypt Traffic – Part 1](https://blog.nviso.eu/2021/10/21/cobalt-strike-using-known-private-keys-to-decrypt-traffic-part-1/)
- [Cobalt Strike: Using Known Private Keys To Decrypt Traffic – Part 2](https://blog.nviso.eu/2021/10/27/cobalt-strike-using-known-private-keys-to-decrypt-traffic-part-2/)
- [Cobalt Strike: Using Process Memory To Decrypt Traffic – Part 3](https://blog.nviso.eu/2021/11/03/cobalt-strike-using-process-memory-to-decrypt-traffic-part-3/)
