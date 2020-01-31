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
        self._client_count = 0
        print(f'Listening for connections on {ConstantVariables.NETWORK_IP}:{ConstantVariables.NETWORK_PORT}...')

    def start(self):

        self._game.start()

        while True:

            read_sockets, _, exception_sockets = select.select(self._sockets_list, [], self._sockets_list)

            for notified_socket in read_sockets:

                # new connection
                if notified_socket == self._server_socket:
                    client_socket, client_address = self._server_socket.accept()
                    client_message = self.receive_message(client_socket)

                    if client_message is False:
                        continue

                    if client_message['data'].decode('utf-8') == "ask_id":
                        self.create_client_and_send_id(client_socket)

                    print('Accepted new connection from {}:{}, request: {}'.format(*client_address,
                                                                                   client_message['data'].decode(
                                                                                       'utf-8')))

                # known connection
                else:

                    message = self.receive_message(notified_socket)

                    if message is False:
                        print('Closed connection from: {}'.format(self._clients[notified_socket]))

                        # remove client
                        for snake in self._game.snakes:
                            if snake.id_client == self._clients[notified_socket]:
                                self._game.snakes.remove(snake)

                        self._sockets_list.remove(notified_socket)
                        del self._clients[notified_socket]
                        continue
                        #

                    client_message = self._clients[notified_socket]
                    print(f"Received message from {client_message}")

                    # update the snake of the client
                    for snake in self._game.snakes:
                        if snake.id_client == client_message:

                            # change direction of the snake
                            snake.direction_current = message['data'].decode('utf-8')

                            # move the snake
                            snake.move_head()
                            if self._game.is_apple_caught(snake):
                                self._game.create_new_apple()
                                snake.growth()
                            else:
                                snake.move_body()

                            # if the client has lost the game
                            if self.is_client_lost(snake):
                                # send to client
                                message_game = "".encode('utf-8')
                                message_game = bytes(f"{len(message_game):<{self._header_length}}",
                                                     'utf-8') + message_game
                                notified_socket.send(message_game)

                                # remove client
                                print('Closed connection from: {}'.format(self._clients[notified_socket]))
                                self._game.snakes.remove(snake)
                                self._sockets_list.remove(notified_socket)
                                del self._clients[notified_socket]
                                break

                    # send game to the client
                    message_game = pickle.dumps(self._game)
                    message_game = bytes(f"{len(message_game):<{self._header_length}}", 'utf-8') + message_game
                    notified_socket.send(message_game)

            # remove clients of the notifications
            for notified_socket in exception_sockets:
                self._sockets_list.remove(notified_socket)
                del self._clients[notified_socket]

    def receive_message(self, client_socket):
        try:
            message_header = client_socket.recv(self._header_length)

            if not len(message_header):
                # if no data receive, client closed connection
                return False

            message_length = int(message_header.decode('utf-8').strip())

            message = client_socket.recv(message_length)

            return {'header': message_header, 'data': message}

        except:
            return False

    def create_client_and_send_id(self, client_socket):
        self._client_count += 1
        client_id = str(self._client_count)  # the id must be a str for sending
        self._clients[client_socket] = client_id

        # creation of the snake of the client
        self._game.create_snake(client_id)
        # add the client id ine the list of clients
        self._sockets_list.append(client_socket)

        # send the id to the client
        message = client_id.encode('utf-8')
        message_header = f"{len(message):<{self._header_length}}".encode('utf-8')
        client_socket.send(message_header + message)

    def is_client_lost(self, snake_client):
        for snake in self._game.snakes:
            if snake != snake_client:
                if snake.get_head_coordinate() == snake_client.get_head_coordinate():
                    return True
                elif snake_client.get_head_coordinate() in snake.body_coordinates:
                    return True
            else:
                if snake.get_head_coordinate() in snake.body_coordinates:
                    return True
        return False
