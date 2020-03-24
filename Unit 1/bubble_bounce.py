from tkinter import *

WIDTH = 600
HEIGHT = 400
SIZE = 20

def lmc_task(event):
    canvas.create_oval(event.x-SIZE/2, event.y-SIZE/2, event.x+SIZE/2, event.y+SIZE/2, fill="orange")

# **** Create Window ****
root = Tk()
#root.geometry("600x400")
root.title("Bouncing Bubbles")

# **** Add to window ****
canvas = Canvas(root, bg="black", width=WIDTH, height=HEIGHT)
canvas.pack()
canvas.bind("<Button-1>", lmc_task)


# **** Run window loop ****
root.mainloop()