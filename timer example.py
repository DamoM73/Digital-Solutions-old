import tkinter as tk
from playsound import playsound

def reduce_one_sec():
    global time_remaining
    if time_remaining > 0:
        time_remaining -= 1
        time_remaining_lb.config(text=str(time_remaining))
        root.update()
        root.after(1000,reduce_one_sec)
    else:
        playsound("Alarm_Clock.mp3")

time_remaining = 10

root = tk.Tk()
root.geometry("800x300")

time_remaining_lb = tk.Label(root, text = str(time_remaining))
time_remaining_lb.pack()

# ***** MAIN PROGRAM *****
root.after(1000,reduce_one_sec)
root.mainloop()