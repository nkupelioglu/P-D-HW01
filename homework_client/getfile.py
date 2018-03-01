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

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
path = "/home/deneme2/Desktop/py_app_files/"
message = raw_input()
server_address = ('192.168.56.101', 3002)
sock.connect(server_address)
sock.send(message)
sock.shutdown(socket.SHUT_WR)
data = sock.recv(32)
md5fromserver = data
generaldata = b""
print 'Server MD5: ' + md5fromserver
while data:
	data = sock.recv(1024)
	generaldata += data

if(md5fromserver.strip() != "nf"):
	f = open(path + message,"w+")
	f.write(generaldata)
	f.close()
	md5local = md5(path + message)
	print 'Calculated MD5: ' +  md5local
	if md5fromserver == md5local:
		print 'File succesfully transferred!'

