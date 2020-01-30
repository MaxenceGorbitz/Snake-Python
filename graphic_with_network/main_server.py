import random
import time

from graphic_with_network.ServerSocket import ServerSocket


random.seed(time.time())
server = ServerSocket()
server.start()
