import tkinter as tk

# STYLING
BTN_SIZE = 7

def passing():
    pass

# ***** CREATE WINDOW *****
root = tk.Tk()
root.geometry("1920x1080")
root.title("Robotics Scoreboard")
root.attributes("-fullscreen", True)
root.configure(bg="#FFFFFF")

# ***** Window Content *****
# *** Title ***
title_fr = tk.Frame(root, bg="#FFFFFF")
title_fr.pack(expand="Y", fill=tk.X)
tk.Label(title_fr, text="Moreton Bay Colleges' Robotics Program", font=("Arial",50), bg="#FFFFFF", fg="#545F66").pack()

# *** Middle Panel ***
middle_fr = tk.Frame(root)
middle_fr.pack(expand="Y", fill=tk.BOTH)

# *** Left middle frame ***
left_middle_fr = tk.Frame(middle_fr, bg="#FFFFFF")
left_middle_fr.grid(column=0, row=0)

red_team_lb = tk.Label(left_middle_fr, text="Red Team", font=("Arial", 40), bg="#FFFFFF", fg="#BA014E")
red_team_lb.grid(row=0, column=0, columnspan=3)

red_score_lb = tk.Label(left_middle_fr,text="0", font=("Arial", 200), bg="#FFFFFF", fg="#BA014E")
red_score_lb.grid(row=1, column=0, columnspan=3)

red_points_1_btn = tk.Button(left_middle_fr,text="0", font=("Arial", 30), bg="#FFFFFF", fg="#BA014E", width=BTN_SIZE,command=passing)
red_points_1_btn.grid(row=2, column=0)

red_points_2_btn = tk.Button(left_middle_fr,text="0", font=("Arial", 30), bg="#FFFFFF", fg="#BA014E", width=BTN_SIZE,command=passing)
red_points_2_btn.grid(row=2, column=1)

red_points_3_btn = tk.Button(left_middle_fr,text="0", font=("Arial", 30), bg="#FFFFFF", fg="#BA014E", width=BTN_SIZE,command=passing)
red_points_3_btn.grid(row=2, column=2)

# *** middle middle frame ***
time_lb = tk.Label(middle_fr, text="3:00", font=("Arial",300), bg="#FFFFFF", fg="#545F66")
time_lb.grid(row=0, column=1, padx=55)

# *** right middle frame
right_middle_fr = tk.Frame(middle_fr, bg="#FFFFFF")
right_middle_fr.grid(column=2, row=0)

blue_team_lb = tk.Label(right_middle_fr, text="Blue Team", font=("Arial", 40), bg="#FFFFFF", fg="#00AEEF")
blue_team_lb.grid(row=0, column=0, columnspan=3)

blue_score_lb = tk.Label(right_middle_fr,text="0", font=("Arial", 200), bg="#FFFFFF", fg="#00AEEF")
blue_score_lb.grid(row=1, column=0, columnspan=3)

blue_points_1_btn = tk.Button(right_middle_fr,text="0", font=("Arial", 30), bg="#FFFFFF", fg="#00AEEF", width=BTN_SIZE,command=passing)
blue_points_1_btn.grid(row=2, column=0)

blue_points_2_btn = tk.Button(right_middle_fr,text="0", font=("Arial", 30), bg="#FFFFFF", fg="#00AEEF", width=BTN_SIZE,command=passing)
blue_points_2_btn.grid(row=2, column=1)

blue_points_3_btn = tk.Button(right_middle_fr,text="0", font=("Arial", 30), bg="#FFFFFF", fg="#00AEEF", width=BTN_SIZE,command=passing)
blue_points_3_btn.grid(row=2, column=2)

# ***** MAIN PROGRAM *****
root.mainloop()
