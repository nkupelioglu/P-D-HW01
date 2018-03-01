import socket
import sys
import hashlib
import os.path

def md5(fname):
	hash_md5 = hashlib.md5()
	with open(fname, "rb") as f:
		for chunk in iter(lambda: f.read(4096), b""):
			hash_md5.update(chunk)
	return hash_md5.hexdigest()


path = "/home/deneme2/Desktop/py_app_files/"
data = b""
file_name = raw_input()
if os.path.isfile(path + file_name):
	md5 = md5(path + file_name)
	f = open(path + file_name, 'rb')
	l = f.read(1024)
	l = l.strip('\n')
	while(l):
		data += l.strip('\n')
		l = f.read(1024)
	f.close()
	message = file_name + '#' + md5 + '#' + data 
	sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	server_address = ('192.168.56.101', 3004)
	sock.connect(server_address)
	sock.send(message)
	sock.shutdown(socket.SHUT_WR)
	back = sock.recv(1024)
	print back.strip()
else:
	print 'File does not exist in folder!' 
