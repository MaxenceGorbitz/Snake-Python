import random
import time

from consol.Game import Game


random.seed(time.time())
game = Game(11, 11)
game.play()



