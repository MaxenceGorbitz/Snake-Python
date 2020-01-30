import socket
import pickle


class Network:
    def __init__(self):
        self._client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self._server = "127.0.0.1"
        self._port = 5555
        self._address = (self._server, self._port)
        self._p = self.connect()

    @property
    def p(self):
        return self._p

    def connect(self):
        try:
            self._client.connect(self._address)
            return self._client.recv(2048).decode()
        except:
            pass

    def send(self, data):
        try:
            self._client.send(str.encode(data))
            return pickle.loads(self._client.recv(2048 * 2))
        except socket.error as e:
            print(e)


# for testing send and receive
"""n = Network()
print(n.send("Hello"))
print(n.send("working"))"""
