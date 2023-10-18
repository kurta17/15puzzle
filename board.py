import turtle as t
class Board():
    def __init__(self):
        self.tiles = [
            [2, 3, 4, 5],
            [10, 11, 12, 13],
            [1, 6, 7, 8],
            [9, 14, 15, 0]  # Use 0 to represent the empty cell
        ]
        self.void_pos = (3, 3)

    def up(self):
        up_to_void_pos = (self.void_pos[0] - 1, self.void_pos[1])
        self.swap_with_void(up_to_void_pos)
        self.draw_tiles()  
    
    def down(self):
        up_to_void_pos = (self.void_pos[0] + 1, self.void_pos[1])
        self.swap_with_void(up_to_void_pos)
        self.draw_tiles()  

    def left(self):
        up_to_void_pos = (self.void_pos[0] , self.void_pos[1] -1)
        self.swap_with_void(up_to_void_pos)
        self.draw_tiles()

    def right(self):
        up_to_void_pos = (self.void_pos[0] , self.void_pos[1] + 1)
        self.swap_with_void(up_to_void_pos)
        self.draw_tiles()


    def swap_with_void(self, int_pos):
        x1, y1 = int_pos
        x2, y2 = self.void_pos
        if 0 <= x1 < len(self.tiles[1]) and 0 <= y1 < len(self.tiles[0]) :
            if (x1 == x2 and (y1 == y2 - 1 or y1 == y2 + 1)) or ((x1 == x2 - 1 or x1 == x2 + 1) and y1 == y2):
                self.tiles[x2][y2], self.tiles[x1][y1] = self.tiles[x1][y1], self.tiles[x2][y2]
                self.void_pos = (x1, y1) 

    def draw_grid(self):
        grid = t.Turtle()
        grid.penup()
        grid.hideturtle()
        grid.speed(0)

        x, y = -125, 135
        
        for row in self.tiles:
            for tile in row:
                grid.goto(x, y)
                grid.pendown()
                grid.forward(50)
                grid.right(90)
                grid.forward(50)
                grid.right(90)
                grid.forward(50)
                grid.right(90)
                grid.forward(50)
                grid.right(90)
                grid.penup()
                x += 50
            x = -125
            y -= 50

    def draw_tiles(self):
        t.clear()
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