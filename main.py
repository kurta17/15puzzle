import turtle as t
from board import Board
screen = t.Screen()
screen.setup(600,600)
screen.tracer(1)
board = Board()
board.draw_tiles()
screen.update()

t.done()