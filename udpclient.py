import socket
import sys

host = 'localhost'
port = 1024

# create socket
print('# Creating socket')
try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
except socket.error:
    print('Failed to create socket')
    sys.exit()

print('# Getting remote IP address') 
try:
    remote_ip = socket.gethostbyname( host )
except socket.gaierror:
    print('Hostname could not be resolved. Exiting')
    sys.exit()

# Connect to remote server
print('# Connecting to server, ' + host + ' (' + remote_ip + ')')
s.connect((remote_ip , port))

# Get text input from the user
sentence = input('Input lowercase sentence:')


# Send data to remote server
print('# Sending data to server')
request = (sentence.encode())

try:
    s.sendall(request)
except socket.error:
    print ('Send failed')
    sys.exit()

# Receive data
print('# Receiving data from server')
full_reply = ''
while True:
    reply = s.recv(8)
    if len(reply) == 0:
        break
    full_reply += reply.decode()

print (full_reply)

print('# Finished!')