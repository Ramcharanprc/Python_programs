# Creating local server.
import socket

socketObj = socket.socket()
print('Socket created successfully.')
port = 221
socketObj.bind(('', port))
print('Socket binded to port: ' + str(port))
socketObj.listen(10)
print('Socket is listening.')
while True:
	client, address = socketObj.accept()
	message = "Welcome to Ram's server."
	print('Got connection from ' + str(address))
	# client.send(message.encode('utf-8'))
	fileName = client.recv(1024).decode('utf-8')
	with open(fileName, 'r') as fpFile:
		data = fpFile.readlines()
		for line in data:
			client.send(line.encode('utf-8'))
	client.close()
socketObj.close()
