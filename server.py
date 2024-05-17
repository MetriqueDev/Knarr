import socket
import threading

def handle_client(c):
    message = c.recv(1024)
    print('Received:', message)
    c.send(b'Echo:' + message)
    c.close()

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('', 81))
s.listen(5)

while True:
    c, addr = s.accept()
    print('Got connection from', addr)
    threading.Thread(target=handle_client, args=(c,)).start()

# Output:
# Got connection from ('127.0.0.1', 52617)
# Received: b'Hello, Server!'
# ...
