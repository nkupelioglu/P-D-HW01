import socket
import sys
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
message = '1'
server_address = ('192.168.56.101', 3001)
sock.connect(server_address)
sock.send(message)
sock.shutdown(socket.SHUT_WR)
data = sock.recv(1024)
print data
