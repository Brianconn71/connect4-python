from Player import *
from GridPosition import *
from Grid import *
from Game import *

grid = Grid(6,7)
game = Game(grid, 4, 2)
game.play()