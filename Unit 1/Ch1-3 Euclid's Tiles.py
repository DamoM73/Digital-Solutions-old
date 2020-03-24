from tkinter import *

# CONSTANTS
WIDTH = 800     # the canvas width
HEIGHT = 600    # the canvas height

# FUNCTIONS
# calcuate tile size
def calculate_tile_size(long_side, short_side):
    # calculates the size of the side of the tile
    remainder = long_side % short_side      # calucate remainder
    while remainder != 0:
        remainder = long_side % short_side
        long_side = short_side
        short_side = remainder

    return long_side

# display the floor
def floor_display(room_long, room_short, tile, floor_canvas):
    # calcualte variables
    number_of_tiles_X = room_long // tile
    number_of_tiles_Y = room_short // tile
    x1 = 0
    y1 = 0

    # generate tiles on canvas
    for count_y_tiles in range(0, number_of_tiles_Y):
        for count_x_tiles in range(0,number_of_tiles_X):
            x2 = x1 + tile
            y2 = y1 + tile
            floor_canvas.create_rectangle(x1,y1,x2,y2, fill="Pink")
            x1 = x2
        y1 = y1 + tile
        x1 = 0

# display tile size
def tile_info_text(room_long, room_short, tile, floor_canvas):
    number_of_tiles_X = room_long // tile
    number_of_tiles_Y = room_short // tile
    number_of_tiles = number_of_tiles_X * number_of_tiles_Y

    floor_canvas.create_text(WIDTH / 2, HEIGHT - 40, \
        text="Your perfect tile has a side of "+ str(tile) +" cm.")
    floor_canvas.create_text(WIDTH / 2, HEIGHT -20, \
        text="You will need " + str(number_of_tiles) + " tiles.")

# ---- MAIN PROGRAM ----
# Initialise window
window = Tk()
window.title("Euclid's Tiles")
canvas = Canvas(window, width=WIDTH, height=HEIGHT)
canvas.pack()

room_length = int(input("Room length: "))
room_width = int(input("Room width: "))
tile_size = calculate_tile_size(room_length,room_width)
#print(tile_size)
floor_display(room_length,room_width,tile_size,canvas)
tile_info_text(room_length,room_width,tile_size,canvas)

window.mainloop()