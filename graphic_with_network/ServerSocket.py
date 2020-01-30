import socket
import select
import time
import pickle

from graphic_with_network.ConstantVariables import ConstantVariables
from graphic_with_network.GameServer import GameServer


class ServerSocket:
    def __init__(self):
        self._header_length = ConstantVariables.NETWORK_HEADER_LENGTH
        self._server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self._server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self._server_socket.bind((ConstantVariables.NETWORK_IP, ConstantVariables.NETWORK_PORT))
        self._server_socket.listen()
        self._sockets_list = [self._server_socket]
        self._clients = {}
        self._game = GameServer()
        print(f'Listening for connections on {ConstantVariables.NETWORK_IP}:{ConstantVariables.NETWORK_PORT}...')

    def start(self):

        self._game.start()

        while True:

            read_sockets, _, exception_sockets = select.select(self._sockets_list, [], self._sockets_list)

            for notified_socket in read_sockets:

                # new connection
                if notified_socket == self._server_socket:
                    client_socket, client_address = self._server_socket.accept()
                    user = self.receive_message(client_socket)

                    if user is False:
                        continue

                    self._sockets_list.append(client_socket)

                    self._clients[client_socket] = user

                    print('Accepted new connection from {}:{}, direction: {}'.format(*client_address,
                                                                                    user['data'].decode('utf-8')))

                # known connection
                else:
                    # TODO receive message to change snakes direction
                    message = self.receive_message(notified_socket)

                    if message is False:
                        print('Closed connection from: {}'.format(self._clients[notified_socket]['data'].decode('utf-8')))

                        # remove client
                        self._sockets_list.remove(notified_socket)
                        del self._clients[notified_socket]
                        continue

                    user = self._clients[notified_socket]
                    print(f"Received message from {user['data'].decode('utf-8')}: {message['data'].decode('utf-8')}")

                    for client_socket in self._clients:
                        if client_socket != self._server_socket:
                            # TODO send game
                            msg = pickle.dumps(self._game)
                            # msg = "toto"
                            msg = bytes(f"{len(message):<{ConstantVariables.NETWORK_HEADER_LENGTH}}", 'utf-8') + msg
                            client_socket.send(msg)

            for notified_socket in exception_sockets:
                self._sockets_list.remove(notified_socket)
                del self._clients[notified_socket]

            self._game.update_pos()

    def receive_message(self, client_socket):
        try:
            message_header = client_socket.recv(self._header_length)

            if not len(message_header):
                # if no data receive, client closed connection
                return False

            message_length = int(message_header.decode('utf-8').strip())

            return {'header': message_header, 'data': client_socket.recv(message_length)}

        except:
            return False
