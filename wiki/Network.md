# Network

- [LAN](#lan)
- [Nmap](#nmap)
- [Packet](#packet)

## LAN
```
sudo arp
Address                  HWtype  HWaddress           Flags Mask            Iface
NameHost                 ether   xx:xx:xx:xx:xx:xx   C                     INTRFC
```

## Nmap
```
nmap -A ip
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
