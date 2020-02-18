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

#now keep talking with the client
while 1:
	# receive data from client (data, addr)
	d = s.recvfrom(1024)
	data = d[0]
	addr = d[1]
	
	if not data: 
		break
	
	reply = 'OK...' + data
	
	s.sendto(reply , addr)
	print 'Message[' + addr[0] + ':' + str(addr[1]) + '] - ' + data.strip()
	
s.close()