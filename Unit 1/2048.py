import tkinter as tk
import colours as c

class Game(tk.Frame):
    def __init__(self):
        self.grid()
        self.master.title("2048")
        self.main_grid = tk.Frame(
            self, bg=c.GRID_COLOUR,bd=3,width=600,height=600
            )
        self.main_grid.grid(pady=(100,0))

    def make_gui(self)

