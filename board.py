import turtle as t
class Board():
    def __init__(self):
        self.tiles = [[2,3,4,5],
                      [10,11,12,13],
                      [1,6,7,8],
                      [9,14,15,None]]
    
    def draw_tiles(self):
        t.penup()
        t.hideturtle()
        t.goto(-100,100)
        t.penup()
        for row in self.tiles:
            for tile in row:
                t.write(tile, align="center", font=("Arial", 14, "normal"))
                t.forward(50)
            t.backward(200)
            t.right(90)
            t.forward(50)
            t.left(90)