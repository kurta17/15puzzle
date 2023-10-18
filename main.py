import turtle as t
from board import Board
screen = t.Screen()
screen.setup(600,600)
screen.tracer(0)
board = Board()
board.draw_tiles()
board.draw_grid()

screen.listen()
screen.onkey(fun=board.up , key="Up")
screen.onkey(fun=board.down , key="Down")
screen.onkey(fun=board.left , key="Left")
screen.onkey(fun=board.right , key="Right")


screen.update()

t.done()