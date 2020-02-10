# Accessing socket.
import socket

socketObj = socket.socket()
ipAddress = (input('Enter Socket IP address: '))
port = int(input('Enter Socket Port number: '))
socketObj.connect((ipAddress, port))
# print(socketObj.recv(1024).decode("utf-8"))
socketObj.send(('menu.cfg').encode('utf-8'))
line = socketObj.recv(1024).decode('utf-8')
text = ''
while(line):
	line = socketObj.recv(1024).decode('utf-8')
	text = text + line
print(text)

socketObj.close()