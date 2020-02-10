# Creating local server.
import socket

socketObj = socket.socket()
print('Socket created successfully.')
port = 944
socketObj.bind(('', port))
print('Socket binded to port: ' + str(port))
socketObj.listen(10)
print('Socket is listining.')
while True:
	c, adrr = socketObj.accept()
	c.send('Welcome to Ram socket.')
	c.close()