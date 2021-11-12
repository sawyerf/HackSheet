# General

- [SCP](#scp)
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
