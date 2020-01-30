import socket
import pickle
import time
from graphic_with_network.GameServer import GameServer

from graphic_with_network.ConstantVariables import ConstantVariables


class ClientSocket:
    def __init__(self):
        self._header_length = ConstantVariables.NETWORK_HEADER_LENGTH
        self._client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def connect(self):
        # connect
        self._client_socket.connect((ConstantVariables.NETWORK_IP, ConstantVariables.NETWORK_PORT))

    def send_and_get_data(self, direction):
        # send direction
        message = direction.encode('utf-8')
        message = "hello".encode('utf-8')
        message_header = f"{len(message):<{self._header_length}}".encode('utf-8')
        self._client_socket.send(message_header + message)

        # receive data
        try:
            while True:
                data_header = self._client_socket.recv(self._header_size)
                if not len(data_header):
                    print("Connection closed by the server")

                data_length = int(data_header.decode('utf-8').strip())

                data = self._client_socket.recv(data_length)
                game = pickle.loads(data)
                return game
        except:
            return GameServer()

    """def receive(self):

        print("Client started!")

        message_length = 0

        while True:
            full_message = b''
            new_message = True
            while True:
                message = self._client_socket.recv(16)
                if new_message:
                    print("new msg len:", message[:self._header_size])
                    message_length = int(message[:self._header_size])
                    new_message = False

                print(f"full message length: {message_length}")

                full_message += message

                print(len(full_message))

                if len(full_message) - self._header_size == message_length:
                    print("full msg recvd")
                    print(full_message[self._header_size:])
                    print(pickle.loads(full_message[self._header_size:]))
                    new_message = True
                    full_message = b""
                    """

    def send_a_message(self):
        message = "hello".encode('utf-8')
        message_header = f"{len(message):<{self._header_length}}".encode('utf-8')
        self._client_socket.send(message_header + message)
