''' Example of how to animate in tkinter '''
from tkinter import *
import random

WIDTH = 600
HEIGHT = 400
SIZE = 10

speedy = random.randrange(-10,10)
speedx = random.randrange(-10,10)

# **** Functions ****
def update_ball():
    global speedy, speedx
    pos = main_canvas.coords(ball)
    if pos[3] >= HEIGHT or pos[1] <= 0:
        speedy = speedy * -1
    if pos[0] <= 0 or pos[2] >= WIDTH:
        speedx = speedx * -1
    main_canvas.move(ball, speedx, speedy)
    root.after(50,update_ball)

# **** Create Window ****
root = Tk()
root.title("Animation Example")

# **** Add content to window ****
main_canvas = Canvas(root, width=WIDTH, height=HEIGHT, bg="black")
main_canvas.pack()
ball = main_canvas.create_oval(WIDTH/2-SIZE, HEIGHT/2-SIZE, WIDTH/2+SIZE, HEIGHT/2+SIZE, fill="orange")

# **** Run window loop ****
root.after(50,update_ball)
root.mainloop()