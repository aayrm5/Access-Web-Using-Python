# making a connection with the socket.
import socket
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('data.pr4e.org',80))

# $telnet data.pr4e.org 80

# GET http://data.pr4e.org/page1.htm HTTP/1.0

cmd = 'GET http://data.pr4e.org/intro-short.txt HTTP/1.0\r\n\r\n'.encode() 
#Above .encode() converts the UNICODE to bytes(either into UTF-8 or ASCII)
mysock.send(cmd) #cmd has info in bytes.

while True:
    data = mysock.recv(512) # Requesting for 512 chars.
    if(len(data) < 1): #If the data has a length less than 1, the loop breaks!
        break
    print(data.decode())#Later info is converted into UNICODE
mysock.close() #retrieves the data in the webpage via data variable and closes the socket. 

