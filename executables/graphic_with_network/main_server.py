import random
import time

from ServerSocket import ServerSocket


random.seed(time.time())
server = ServerSocket()
server.start()
