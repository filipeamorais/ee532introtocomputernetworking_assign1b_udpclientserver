import socket
import sys

host = 'localhost'
port = 1024

# create dgram udp socket
print('# Creating socket')
try:
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
except socket.error:
    print('Failed to create socket')
    sys.exit()

# main loop 
while(1) :
    msg = raw_input('Enter message to send : ')

    print('# Sending data to server')
    try :
		#Send the whole string
		s.sendto(msg, (host, port))

        # Receive data
        print('# Receiving data from server')
        full_reply = ''
        while True:
            reply = s.recvfrom(8)
            if len(reply) == 0:
                break
            full_reply += reply.decode()

        print (full_reply)

        print('# Finished!')

    except socket.error, msg:
		print 'Error Code : ' + str(msg[0]) + ' Message ' + msg[1]
		sys.exit()