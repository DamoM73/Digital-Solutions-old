import tkinter as tk

# ***** GLOBAL VARIABLES *****
current_time = 0
running = False

def time_to_str(time_val):
    # converts time into H:MM:SS formatted string
    sec_in_hour = 3600
    sec_in_min = 60
    
    # calculate values
    hours = time_val // sec_in_hour
    minutes = (time_val % sec_in_hour) // sec_in_min
    seconds = (time_val % sec_in_hour) % sec_in_min

    # format values
    hours = str(hours)
    if minutes < 10:
        minutes = "0"+str(minutes)
    else:
        minutes = str(minutes)
    if seconds < 10:
        seconds = "0"+str(seconds)
    else:
        seconds = str(seconds)

    # return formatted time
    return hours+":"+minutes+":"+seconds

def start():
    # starts the timer 
    global running
    running = True
    
def reset():
    # stops the timer and changes the time to 0
    global running, current_time
    running = False
    current_time = 0
    time_lb.config(text=time_to_str(current_time))
    root.update()

def stop():
    # stops the timer
    global running
    running = False

def go():
    # will increase the time and update the display.
    global current_time
    if running:
        current_time += 1
        time_lb.config(text=time_to_str(current_time))
        root.update()
    root.after(1000,go)             # after 1 second, run this function again

    


# ***** CREATE WINDOW *****
root = tk.Tk()
root.title("Stop Watch")

# *** Window content ***
time_lb = tk.Label(root, text=time_to_str(current_time),font=("Arial",200))
time_lb.grid(row=0,column=0,columnspan=3)

start_btn = tk.Button(root, text="Start", width=10, font=("Arial",50), bg="GREEN", command=start)
start_btn.grid(row=1,column=0)

reset_btn = tk.Button(root, text="Reset", width=10, font=("Arial",50), bg="ORANGE", command=reset)
reset_btn.grid(row=1,column=1)

stop_btn = tk.Button(root, text="Stop", width=10, font=("Arial",50), bg="RED", command=stop)
stop_btn.grid(row=1,column=2)

# **** MAIN PROGRAM ****
root.after(1000,go)                 # after 1 second run the go function
root.mainloop()