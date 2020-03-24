from tkinter import *

HEIGHT = 400
WIDTH = 600
SIZE = 10

def lmc(event):
    Ball(event.x, event.y)

class Ball:
    def __init__(self, x, y):
        self.ball = main_canvas.create_oval(x-SIZE,y-SIZE,x+SIZE,y+SIZE, fill="red")
        self.speed = 0
        self.update_ball()

    def update_ball(self):
        
        main_canvas.move(self.ball,0,self.speed)
        pos = main_canvas.coords(self.ball)
        print(self.speed)
        
        if pos[3] >= HEIGHT:
            if self.speed > 1:
                print("bounce")
                self.speed = (self.speed - 2) * -1
            elif self.speed == 1:
                self.speed = 0

        else:
            self.speed += 1
        root.after(50,self.update_ball)


# **** create window ****
root = Tk()
root.title("Bouncing ball")

# **** add content to window ****
main_canvas = Canvas(root, width=WIDTH, height=HEIGHT)
main_canvas.pack()
main_canvas.bind("<Button-1>", lmc)

# **** run window loop ****
root.mainloop()