import tkinter as tk

# STYLING
BTN_SIZE = 7

TITLE_FTN = ("Arial",75)
TEAM_FNT = ("Arial", 40)
SCORE_FTN = ("Arial", 300)
TIME_FNT = ("Arial", 300)
BUTTON_FNT = ("Arial", 30)

MBCS_BLUE = "#00AEEF"
MBCS_RED = "#BA014E"
MBCS_WHITE = "#FFFFFF"
MBCS_GREY = "#545F66"

def passing():
    pass

def close():
    root.destroy()

# ***** GLOBAL VARIABLES *****
points = [0,0,0]
time = 0
red_score = 0
blue_score = 0

# ***** CREATE WINDOW *****
root = tk.Tk()
root.geometry("1920x1080")
root.title("Robotics Scoreboard")
root.attributes("-fullscreen", True)
root.configure(bg=MBCS_WHITE)

# ***** Window Content *****
# *** Title ***
title_fr = tk.Frame(root, bg=MBCS_WHITE)
title_fr.pack(expand="Y", fill=tk.X)
tk.Label(title_fr, text="Moreton Bay Colleges' Robotics Program", font = TITLE_FTN, bg=MBCS_WHITE, fg=MBCS_GREY).pack()

# *** Middle Panel ***
middle_fr = tk.Frame(root, bg=MBCS_WHITE)
middle_fr.pack(expand="Y", fill=tk.BOTH)

# *** Left middle frame ***
left_middle_fr = tk.Frame(middle_fr, bg=MBCS_WHITE)
left_middle_fr.grid(column=0, row=0)

red_team_lb = tk.Label(left_middle_fr, text="Red Team", font=TEAM_FNT, bg=MBCS_WHITE, fg=MBCS_RED)
red_team_lb.grid(row=0, column=0, columnspan=3)

red_score_lb = tk.Label(left_middle_fr,text="0", font=SCORE_FTN, bg=MBCS_WHITE, fg=MBCS_RED)
red_score_lb.grid(row=1, column=0, columnspan=3)

red_points_1_btn = tk.Button(left_middle_fr,text="0", font=BUTTON_FNT, bg=MBCS_WHITE, fg=MBCS_RED, width=BTN_SIZE, relief=tk.FLAT, command=passing)
red_points_1_btn.grid(row=2, column=0)

red_points_2_btn = tk.Button(left_middle_fr,text="0", font=BUTTON_FNT, bg=MBCS_WHITE, fg=MBCS_RED, width=BTN_SIZE, relief=tk.FLAT, command=passing)
red_points_2_btn.grid(row=2, column=1)

red_points_3_btn = tk.Button(left_middle_fr,text="0", font=BUTTON_FNT, bg=MBCS_WHITE, fg=MBCS_RED, width=BTN_SIZE, relief=tk.FLAT, command=passing)
red_points_3_btn.grid(row=2, column=2)

# *** middle middle frame ***
timer_fr = tk.Frame(middle_fr, bg=MBCS_WHITE)
timer_fr.grid(row=0, column=1)

tk.Label(timer_fr, text=" ", font=("Arial",40),bg=MBCS_WHITE).grid(row=0,column=0)

time_lb = tk.Label(timer_fr, text="3:00", font=TIME_FNT, bg=MBCS_WHITE, fg=MBCS_GREY)
time_lb.grid(row=1, column=0, columnspan=3, padx=55)

start_btn = tk.Button(timer_fr, text="Start", font=("Arial",30), bg="GREEN", width=BTN_SIZE, relief=tk.FLAT, command=passing)
start_btn.grid(row=2,column=0)

stop_btn = tk.Button(timer_fr, text="Stop", font=("Arial",30), bg="RED", width=BTN_SIZE, relief=tk.FLAT, command=passing)
stop_btn.grid(row=2,column=1)

reset_btn = tk.Button(timer_fr, text="Reset", font=("Arial",30), bg="ORANGE", width=BTN_SIZE, relief=tk.FLAT, command=passing)
reset_btn.grid(row=2,column=2)

# *** right middle frame
right_middle_fr = tk.Frame(middle_fr, bg=MBCS_WHITE)
right_middle_fr.grid(column=2, row=0)

blue_team_lb = tk.Label(right_middle_fr, text="Blue Team", font=TEAM_FNT, bg=MBCS_WHITE, fg=MBCS_BLUE)
blue_team_lb.grid(row=0, column=0, columnspan=3)

blue_score_lb = tk.Label(right_middle_fr,text="0", font=SCORE_FTN, bg=MBCS_WHITE, fg=MBCS_BLUE)
blue_score_lb.grid(row=1, column=0, columnspan=3)

blue_points_1_btn = tk.Button(right_middle_fr,text="0", font=BUTTON_FNT, bg=MBCS_WHITE, fg=MBCS_BLUE, width=BTN_SIZE, relief=tk.FLAT,command=passing)
blue_points_1_btn.grid(row=2, column=0)

blue_points_2_btn = tk.Button(right_middle_fr,text="0", font=BUTTON_FNT, bg=MBCS_WHITE, fg=MBCS_BLUE, width=BTN_SIZE, relief=tk.FLAT,command=passing)
blue_points_2_btn.grid(row=2, column=1)

blue_points_3_btn = tk.Button(right_middle_fr,text="0", font=BUTTON_FNT, bg=MBCS_WHITE, fg=MBCS_BLUE, width=BTN_SIZE, relief=tk.FLAT,command=passing)
blue_points_3_btn.grid(row=2, column=2)

# *** Bottom frame ***
bottom_fr = tk.Frame(root, bg=MBCS_WHITE)
bottom_fr.pack()

exit_btn = tk.Button(bottom_fr,text="Exit", font=BUTTON_FNT, bg=MBCS_GREY, fg=MBCS_WHITE, width=BTN_SIZE, relief=tk.FLAT,command=close)
exit_btn.pack()

# ***** MAIN PROGRAM *****
root.mainloop()