import socket
import pickle
from _thread import *
import sys

from graphic_with_network.Game import Game

server = "10.103.120.81"
port = 5555

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    s.bind((server, port))
except socket.error as e:
    str(e)

s.listen(2)
print("Waiting for a connection, Server started")

# connected = set()
game = Game()


def thread_client(connection, player):
    #connection.send(str.encode(str(player)))
    connection.send(pickle.loads(connection.recv(2048 * 2)))
    reply = ""
    while True:
        try:
            # data = connection.recv(4096).decode()
            data = pickle.loads(connection.recv(2048 * 2))
            # reply = data.decode("utf-8")

            if not data:
                print("Disconnected")
                break
            else:
                print("Received: ", reply)
                print("Sending: ", reply)
            # connection.sendall(str.encode(reply))
            print("test")
            tmp = pickle.dumps(game)
            print(tmp)
            connection.sendall(tmp)
        except:
            break

    print("Lost connection")
    connection.close()


current_user = 0

while True:
    # conn : new socket
    # address : address bound to the socket
    conn, address = s.accept()
    print("Connected to: ", address)

    start_new_thread(thread_client, (conn, current_user))
    current_user += 1
