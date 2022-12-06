<picture>
    <source height="100px" srcset="https://user-images.githubusercontent.com/22857002/173634291-a93278a1-aad9-4bac-907b-e1432fba27e0.svg#gh-dark-mode-only" media="(prefers-color-scheme: dark)">
    <img height="100px" src="https://user-images.githubusercontent.com/28403617/172730324-eb7e3c6f-12a9-4388-987d-529fe99e63be.svg#gh-light-mode-only">
</picture>

---

- [DNS](#dns)
- [Hydra](#hydra)
- [List opened port localy](#list-opened-port-localy)
- [NFS](#nfs)
- [Nmap](#nmap)
- [Packet Analyzer](#packet-analyzer)
- [RPCBind](#rpcbind)
- [SNMP](#snmp)
- [Scan Local Network](#scan-local-network)

# Nmap
### Scan Popular Port
```bash
nmap --top-ports 5000 ip
```
### Fast scan
```bash
nmap -T4 -F ip
nmap -sV -T4 -O -F -A --version-light ip
```
### Scan all port 
```bash
nmap -p- -T4 -v ip
```
### Scan With Script & Version
```bash
nmap -A -T4 -sC -sV ip 
```
### Scan All Local
```bash
nmap 192.168.1.1/24 -sn -T4 ip
```
### Scan with scripts
```bash
nmap -sC ip
nmap --script "default,discovery,exploit,version,vuln" ip
nmap --script "default,discovery,exploit,version,vuln,servicetags,ntp-monlist,dns-recursion,snmp-sysdescr" ip
```
### Scan udp
```bash
sudo nmap -sU -T4 ip
sudo nmap -sUV -T4 -F --version-intensity 0 ip
sudo nmap -sU -A -PN -n -pU:19,53,123,161 -script=ntp-monlist,dns-recursion,snmp-sysdescr ip
sudo nmap -sU -pU:19,53,123,161 -Pn -n --max-retries=0 ip
```
### Scan SCTP
```bash
nmap -T4 -sY -n --open -Pn ip
```
### Hardcore scan
```bash
sudo nmap -sS -sU -p- -PN -O -sV -sC --allports --version-all -T4  ip -vv
```

# DNS
> *Port: 53*
>
> Domain Name System (DNS) is the hierarchical and distributed naming system used to identify computers reachable through the Internet. 
> These are most commonly used to map human-friendly domain names to the numerical IP addresses computers need to locate services.

### Any Information
```bash
dig ANY @dns_ip domain
```

### Information
```bash
dig TXT @dns_ip domain
```

### Tranfert Zone
```bash
dig axfr @dns_ip domain
```

### Reverse Lookup
```bash
dig -x ip @dns_ip
```

### Reverse All Address
```bash
dnsrecon -r 127.0.0.0/24 -n ip_dns
```

# SNMP
> *Port: 161 / 162*
> 
> SNMP is used to monitor the network, detect network faults, and sometimes even used to configure remote devices.

### List devices
```bash
snmp-check ip
```

# RPCBind
> The rpcbind utility maps RPC services to the ports on which they listen. RPC processes notify rpcbind when they start, registering the ports they are listening on and the RPC program numbers they expect to serve. - [redhat](https://access.redhat.com/documentation/en-en/red_hat_enterprise_linux/6/html/storage_administration_guide/s2-nfs-methodology-portmap)
> 
> Port: 111

## Info
```
rpcinfo -p ip
```

- [Pentesting NFS Servers](https://medium.com/@minimalist.ascent/pentesting-nfs-servers-a22090e1ec09)

# NFS
>  A Network File System (NFS) allows remote hosts to mount file systems over a network and interact with those file systems as though they are mounted locally. - [redhat](https://access.redhat.com/documentation/en-en/red_hat_enterprise_linux/6/html/storage_administration_guide/ch-nfs)
>
> Port: 2049

> To bypass permission change your uid
### Show NFS
```bash
showmount -e squashed.htb
```

### Mount
```bash
mount -t nfs squashed.htb:/ nsf_mount -o nolock
```

- [Pentesting NFS Servers](https://medium.com/@minimalist.ascent/pentesting-nfs-servers-a22090e1ec09)

# Scan Local Network
> ARP Scannner Tools shows every active IPv4 device on your Subnet. Since ARP is non-routable, this type of scanner only works on the local LAN.
> 
> Address Resolution Protocol (ARP) is the Dynamic mapping technique used to map the logical address (IP) to a physical address (MAC).

### Arp
```bash
sudo arp
Address                  HWtype  HWaddress           Flags Mask            Iface
NameHost                 ether   xx:xx:xx:xx:xx:xx   C                     INTRFC
```

### Netdiscover
```bash
netdiscover
```

### Arp-scan
```bash
arp-scan -l
```

# List opened port localy
### SS
```bash
ss -lntu
```

### Netstat
```bash
netstat -tulpn
```

# Hydra
### Proxy
```bash
export HYDRA_PROXY=connect://localhost:8080
```
### Basic HTTP Auth 
```bash
hydra -C wordlist.txt SERVER_IP -s PORT http-get /
```
### Post HTTP Login
```bash
hydra -l admin -P wordlist.txt -f ip -s port http-post-form "/login.php:username=^USER^&password=^PASS^:F=<form name='login'"
```
### SSH
```bash
hydra -L user.txt -P pass.txt -u -f -t 4 ssh://ip:port
```
### FTP
```bash
hydra -l m.gates -P /usr/share/wordlists/rockyou.txt ftp://127.0.0.1
```

# Packet Analyzer
## Wireshark
### Run
```bash
sudo wireshark
```

### Get all Files
- File > Export Object > HTTP
- Rigth Click On request > Follow > TCP

### Filters
```
smb || smb2 || http || tcp ||
```
```
ip.src == 1.1.1.1 && ip.dst == 1.1.1.1 && tcp.port == 80
```

## TCPflow
### Export File of pcap
```bash
tcpflow -r capture.pcap
```

## Tcpdump
### Basic
```bash
sudo tcpdump -i any
```
### Max Argument
```bash
sudo tcpdump -i any -c <MAX_PACKETS> host 192.168.1.1 '&&' port 80 '&&' src 1.1.1.1
```
### Print HTTP content
```bash
sudo tcpdump -i any -c10 -nn -A port 80
```
### Save
```bash
sudo tcpdump -i any -w file.pcap
```

## Python
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