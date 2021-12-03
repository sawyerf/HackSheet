from pwn import *

# Telnet
sh = remote("ip", 30888)
# SSH:
# sh = ssh('user', 'ip', password='pass', port=22)
# Exec
# process('./exec')

sh.sendline(b'ls')
flag = sh.recvline(timeout=5)
log.success(flag)

sh.interactive()

sh.close()