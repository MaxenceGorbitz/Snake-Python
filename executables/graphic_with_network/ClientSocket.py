import socket
import pickle

from ConstantVariables import ConstantVariables


class ClientSocket:
    def __init__(self):
        self._header_length = ConstantVariables.NETWORK_HEADER_LENGTH
        self._client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self._id = -1

    def connect(self):
        # connect
        self._client_socket.connect((ConstantVariables.NETWORK_IP, ConstantVariables.NETWORK_PORT))

        # send a message to ask a client id from the server
        message = "ask_id".encode('utf-8')
        message_header = f"{len(message):<{self._header_length}}".encode('utf-8')
        self._client_socket.send(message_header + message)

        # receive the response from the server
        # the header
        data_header = self._client_socket.recv(self._header_length)
        if not len(data_header):
            print("Connection closed by the server")
        data_length = int(data_header.decode('utf-8').strip())

        # the data
        id_from_server = self._client_socket.recv(data_length)

        # set the id
        self._id = id_from_server.decode('utf-8')

    def send_direction_and_get_data(self, direction):
        # send direction
        message = direction.encode('utf-8')
        message_header = f"{len(message):<{self._header_length}}".encode('utf-8')
        self._client_socket.send(message_header + message)

        # receive data
        # header
        data_header = self._client_socket.recv(self._header_length)
        if not len(data_header):
            print("Connection closed by the server")

        data_length = int(data_header.decode('utf-8').strip())

        if data_length == 0:
            return None
        else:
            # receive game
            data = self._client_socket.recv(data_length)
            game = pickle.loads(data)
            return game

    @property
    def id(self):
        return self._id
