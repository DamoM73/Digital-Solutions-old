from tkinter import *

# CONSTANTS
WIDTH = 1000
HEIGHT = 600

# GLOBAL VARIABLES
total = 0
fib1 = 0
fib2 = 1
numberOfBubble = 0
x1 = 0
y1 = HEIGHT

# INITIALISE TKINTER
window = Tk()
window.title("Fibonacci Bubbles")
canvas = Canvas(window, width=WIDTH, height=HEIGHT, bg="green")
canvas.pack()


while numberOfBubble < 14:
    total = fib1 + fib2
    fib2 = fib1

    fib1 = total
    diameter = total

    numberOfBubble += 1

    x2 = x1 + diameter
    y2 = HEIGHT - diameter
    canvas.create_oval(x1,y1,x2,y2, fill="blue")
    x1 = x2
    window.update

window.mainloop()