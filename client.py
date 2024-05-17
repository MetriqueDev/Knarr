import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.connect(('localhost', 81))

s.send(b'Hello, Server!')
message = s.recv(1024)
print('Received from server: ', message)

# Output:
# Received from server:  b'Hello, Client!'