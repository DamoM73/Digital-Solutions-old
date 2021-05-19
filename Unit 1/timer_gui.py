import tkinter as tk

def format_time(time):
    minutes = time // 60
    seconds = time % 60
    return f"{minutes}:{seconds}"

def update():
    if root.running:
        root.current_time -= 1
    time_lb.config(text=format_time(root.current_time))
    time_lb.after(1000,update)

def start():
    root.running = True

def pause():
    root.running = False

def reset():
    root.running = False
    root.current_time = root.time

def set_time():
    set_window = tk.Toplevel(root)
    set_window.geometry("200x150")

    tk.Label(set_window, text="Enter time in seconds").grid(row=0,column=0,columnspan=2)

    set_window.time_var = tk.StringVar(set_window, root.time)
    time_txt = tk.Entry(set_window,textvariable=set_window.time_var)
    time_txt.grid(row=1,column=0,columnspan=2)

    def save_time():
        root.time = int(set_window.set_window.time_var.get())
        set_window.destroy()
        set_window.update()

    ok_btn = tk.Button(set_window,text="Ok",command=save_time)
    ok_btn.grid(row=2,column=0)

    cancel_btn = tk.Button(set_window,text="Cancel",command=None)
    cancel_btn.grid(row=2,column=1)




# make window
root = tk.Tk()
root.geometry("400x300")
root.title("Timer")

root.time = 330
root.current_time = root.time
root.running = False

tk.Label(root,text="Timer",font=("Arial",50)).grid(row=0,column=0,columnspan=4)

time_lb = tk.Label(root,text=format_time(root.current_time),font=("Arial",100))
time_lb.grid(row=1,column=0,columnspan=4)

start_btn = tk.Button(root,text="Start",font=("Arial",20),command=start)
start_btn.grid(row=2,column=0)

pause_btn = tk.Button(root,text="Pause",font=("Arial",20),command=pause)
pause_btn.grid(row=2,column=1)

reset_btn = tk.Button(root,text="Reset",font=("Arial",20),command=reset)
reset_btn.grid(row=2,column=2)

set_btn = tk.Button(root,text="Set",font=("Arial",20),command=set_time)
set_btn.grid(row=2,column=3)

# ===== MAIN PROGRAM =====

time_lb.after(1000,update())

tk.mainloop()