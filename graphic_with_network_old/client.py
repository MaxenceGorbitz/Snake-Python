import socket
import select
import errno  # allow to specify error
import sys
import pickle
import pygame
import time

from graphic_with_network_old.ClientPygame import ClientPygame


# init pygame
pygame.init()
pygame.display.set_caption("Snake")
# init socket
"""HEADER_LENGTH = 10
IP = "127.0.0.1"
PORT = 5555

my_username = input("Username: ")
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((IP, PORT))
client_socket.setblocking(False)

username = my_username.encode("utf-8")
username_header = f"{len(username):<{HEADER_LENGTH}}".encode("utf-8")
client_socket.send(username_header + username)"""

# init game
client_pygame = ClientPygame()

while True:
    client_pygame.manage_event()
    client_pygame.draw_screen()
    pygame.display.flip()
    time.sleep(1)
    """message = input(f"{my_username} > ")

    if message:
        message = message.encode("utf-8")
        message_header = f"{len(message):<{HEADER_LENGTH}}".encode("utf-8")
        client_socket.send(message_header + message)

    try:
        while True:
            # receive things
            username_header = client_socket.recv(HEADER_LENGTH)
            if not len(username_header):
                print("connection closed by the server")
                sys.exit()
            username_length = int(username_header.decode("utf-8").strip())
            username = client_socket.recv(username_length).decode("utf-8")

            message_header = client_socket.recv(HEADER_LENGTH)
            message_length = int(message_header.decode("utf-8").strip())
            message = client_socket.recv(message_length).decode("utf-8")

            print(f"{username} > {message}")

    except IOError as e:
        if e.errno != errno.EAGAIN and e.errno != errno.EWOULDBLOCK:
            print('Reading error', str(e))
            sys.exit()
        continue

    except Exception as e:
        print('General error', str(e))
        sys.exit()"""

    """full_msg = b''  # b : bytes
    new_msg = True
    while True:  # to use buffer
        msg = client_socket.recv(16)  # buffer
        if new_msg:
            print("new message length: ", msg[:HEADER_LENGTH])
            msg_len = int(msg[:HEADER_LENGTH])
            new_msg = False

        full_msg += msg

        if len(full_msg) - HEADER_LENGTH == msg_len:
            print("full message recvd")
            print(full_msg[HEADER_LENGTH:])

            d = pickle.loads(full_msg[HEADER_LENGTH:])
            print(d)

            new_msg = True
            full_msg = b''

    print(full_msg)"""
