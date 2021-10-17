import socket
import threading


def findPage(endpoint):
	#translate endpoints to filenames
	if(endpoint == "/home"):
		return "homepage.html"
	elif(endpoint == "/app"):
		return "appPage.html"
	else:
		return ""

def error404(c):
	#send 404 not found response
	response = 'HTTP/1.1 404 NOT FOUND\n\nFile Not Found'
	c.sendall(response.encode())
	
def ok200(c, file_address):
	content = ''
	response = ''
	
	#if filenotfound send error404
	try:
		f = open(file_address, 'rb')
		content = f.read()
		f.close()
		response = 'HTTP/1.1 200 OK\n\n'
		c.sendall(response.encode())
		c.sendall(content)
	except FileNotFoundError:
		error404(c)
	
def newThread(c):
	msg = c.recv(1024).decode('ascii')
	print(msg)
	
	headers = msg.split('\n')
	endpoint = headers[0].split()[1]
	print('\n\n\n')
	print(endpoint)
	file_address = findPage(endpoint)
	print('\n\n\n')
	print(file_address)
	if(file_address == ""):
		error404(c)
	ok200(c, file_address)

def receiveConnection(web_socket):
	
	while True:
		#establish connection
		connection, addr=web_socket.accept()
		
		#create new thread
		threading.Thread(target=newThread, args=(connection,)).start()
		
		
def main(args):
	#initialize server host address
	hostIP = 'localhost'
	hostPort = 26262
	
	#create web socket
	web_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	
	#bind web socket to host address and listen for connections
	web_socket.bind((hostIP, hostPort))
	web_socket.listen()
	
	#Handshake
	receiveConnection(web_socket)
	web_socket.close()
		
		

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
