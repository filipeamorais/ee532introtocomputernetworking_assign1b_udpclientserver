import socket
import sys

serverPort = 1024

# create dgram udp socket
print('# Creating socket')
try:
    serverSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
except socket.error:
    print('Failed to create socket')
    sys.exit()

# create socket
print('# Setting up the server')
try:
    serverSocket.bind(('',serverPort))
except socket.error:
    print('Failed to create socket')
    sys.exit()

#loop to keep talking with the client
while 1:
	
	# receive data from client 
	d = serverSocket.recvfrom(1024)
	data = d[0].decode()
	addr = d[1]
	print('# Received data from client')
	reply = data.upper()
	
	serverSocket.sendto(reply.encode() , addr)
	print ('Message sent [' + addr[0] + ':' + str(addr[1]) + '] - ' + reply)
	
serverSocket.close()