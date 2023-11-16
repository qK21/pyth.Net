import socket 

host = 'google.com'
port = 80 

#create a socket object
client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
#connect the client 
client.connect((host,port))

client.send(b"GET / HTTP/1.1\r\nHOST: google.com\r\n\r\n")

response = client.recv(4096)

print(response.decode())
client.close()