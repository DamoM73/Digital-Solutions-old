import time
import tkinter as tk

TIME = 90
running = False
time_remaining = TIME

def time_to_string(input_time):
    minutes = str(input_time // 60)
    seconds = input_time % 60
    if seconds < 10:
        seconds = "0"+str(seconds)
    else:
        seconds = str(seconds)
    return minutes+":"+seconds

def count_down():
    global time_remaining, running
    if running:
        time_remaining -= 1
        time_lb.config(text=time_to_string(time_remaining))
        root.update()
    if time_remaining == 0:
        running = False
    else:
        root.after(1000,count_down)

def start():
    global running
    running = True

def stop():
    global running
    running = False

def reset():
    global running, time_remaining
    running = False
    time_remaining = TIME
    time_lb.config(text=time_to_string(time_remaining))
    root.update()




# ***** CREATE WINDOW *****
root = tk.Tk()
root.geometry("600x300")
root.title("Countdown Timer")

time_lb = tk.Label(root,text=time_to_string(time_remaining),font=("Arial",100))
time_lb.pack(expand="Y", fill=tk.BOTH)

buttons_fr = tk.Frame(root)
buttons_fr.pack(expand="Y", fill=tk.BOTH, side=tk.TOP)
for index in range(3):
    buttons_fr.columnconfigure(index,weight=1)
buttons_fr.rowconfigure(0,weight=1)

start_btn = tk.Button(buttons_fr, text="Start", width=10, bg="GREEN", command=start)
start_btn.grid(row=0,column=0)

stop_btn = tk.Button(buttons_fr, text="Stop", width=10, bg="RED", command=stop)
stop_btn.grid(row=0,column=1)

reset_btn = tk.Button(buttons_fr, text="Reset", width=10, bg="ORANGE", command=reset)
reset_btn.grid(row=0,column=2)



# ***** MAIN PROGRAM *****
root.after(1000,count_down)
root.mainloop()
