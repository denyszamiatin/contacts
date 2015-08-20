import socket

class NetworkManager(object):
    def __init__(self, port=12346):
        s = socket.socket()
        s.bind(('', port))
        s.listen(1)
        print "Listen {}...".format(port)
        self.c, a = s.accept()
        
    def input(self, prompt):
        self.output(prompt)
        answer = self.c.recv(1024)
        if not answer:
            exit()
        print "Client request: {}".format(answer)
        return answer
        
    def output(self, message):
        self.c.sendall(message)
        
