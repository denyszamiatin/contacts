import socket

s = socket.socket()
s.connect(('', 12346))
while True:
    message = s.recv(1024)
    print message
    if message.endswith('? '):
        request = raw_input()
        s.sendall(request)
