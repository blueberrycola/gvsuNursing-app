import socket
import threading

hitCount = 0
def newThread(c):
	request = c.recv(1024).decode('ascii')
	print(request)
	headers = request.split('\n')
	fileName = headers[0].split()[1]
	fileName = fileName.replace('/', '')

	response = ''
	content = ''
	found = False
	try:
		f = open(fileName, 'rb')
		content = f.read()
		f.close()
		found = True
		response = 'HTTP/1.1 200 OK\n\n'
	except FileNotFoundError:
		response = 'HTTP/1.1 404 NOT FOUND\n\nFile Not Found'
	c.sendall(response.encode())
	if not found:
		print("404 NOT FOUND")
		c.sendall(content.encode())
	else:
		print("200 OK")
		c.sendall(content)
	c.close()

def main():
	serverIP = 'localhost'
	serverPort = 26262
	webSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	webSocket.bind((serverIP, serverPort))
	webSocket.listen()
	while True:
		connection, addr = webSocket.accept()
		threading.Thread(target=newThread, args = (connection,)).start()
	hitCount += 1
	print(hitCount)
	webSocket.close()

if __name__ == "__main__":
	main()
