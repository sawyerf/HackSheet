# 🌐 Network

- [DNS](#dns)
- [LAN](#lan)
- [Nmap](#nmap)
- [Packet](#packet)
- [List opened port localy](#list-opened-port-localy)

## LAN
```
sudo arp
Address                  HWtype  HWaddress           Flags Mask            Iface
NameHost                 ether   xx:xx:xx:xx:xx:xx   C                     INTRFC
```

## Nmap
### Scan Popular Port
```
nmap -A ip
```
### Scan all port 
```
nmap -p- -T4 -v ip
```
### Scan With Script & Version
```
nmap -A -T4 -sC -sV ip 
```
### Scan All Local
```
nmap 192.168.1.1/24 -sn -T4 
```

## DNS
### Any Information
```
dig ANY @dns_ip domain
```

### Reverse Lookup
```
dig -x ip @dns_ip
```

### Reverse All Address
```
dnsrecon -r 127.0.0.0/24 -n ip_dns
```

## List opened port localy

### ss

```
ss -lntu
```

### netstat

#### Linux

```
netstat -tulpn
```

#### FreeBSD/MacOS X

```
netstat -anp tcp
netstat -anp udp
```

#### Openbsd

```
netstat -na -f inet
netstat -nat
```

## Hydra
### Proxy
```
export HYDRA_PROXY=connect://localhost:8080
```
### Basic HTTP Auth 
```
hydra -C wordlist.txt SERVER_IP -s PORT http-get /
```
### Post HTTP Login
```
hydra -l admin -P wordlist.txt -f ip -s port http-post-form "/login.php:username=^USER^&password=^PASS^:F=<form name='login'"
```
### SSH
```
hydra -L user.txt -P pass.txt -u -f -t 4 ssh://ip:port
```
### FTP
```
hydra -l m.gates -P /usr/share/wordlists/rockyou.txt ftp://127.0.0.1
```

## Packet
### Wireshark
#### Run
```
sudo wireshark
```
#### Get all Files
- File > Export Object > HTTP
- Rigth Click On request > Follow > TCP

#### Filters
```
smb || smb2 || http || tcp ||
```
```
ip.src == 1.1.1.1 && ip.dst == 1.1.1.1 && tcp.port == 80
```

### TCPflow
#### Export File of pcap
```
tcpflow -r capture.pcap
```

### Tcpdump
#### Basic
```
sudo tcpdump -i any
```
#### Max Argument
```
sudo tcpdump -i any -c <MAX_PACKETS> host 192.168.1.1 '&&' port 80 '&&' src 1.1.1.1
```
#### Print HTTP content
```
sudo tcpdump -i any -c10 -nn -A port 80
```
#### Save
```
sudo tcpdump -i any -w file.pcap
```

### Python
```python
from scapy.all import *

scapy_cap = rdpcap('file.pcap')
i = 0
for packet in scapy_cap:
	if type(packet[TCP].payload) == scapy.packet.Raw:
		try:
			print(i, ':', packet[TCP].payload.load.decode())
		except:
			print(i, ':', packet[TCP].payload.load)
	i += 1
```