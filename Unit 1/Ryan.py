from tkinter import *

root = Tk()
root.geometry("1200x800")
root.title("Robotics Scoreboard")
root.grid_propagate(0)

Label(root,text="Robot Competition Scoreboard", font=("Arial",50,"bold")).grid(row=0,column=0)

centre_fr = Frame(root)
centre_fr.grid(row=1,column=0)


# ----- Blue Team Frame -----
blue_team_fr = Frame(centre_fr, bg="#00aeef", width=400, height=400)
blue_team_fr.grid(row=0,column=0)

blue_team_name = Label(blue_team_fr, text = "Blue Team", font=("Arial",20,"bold"), bg="#00aeef")
blue_team_name.grid(row=0,column=0)

blue_team_score = Label(blue_team_fr, text="0", font=("Arial",50,"bold"), bg="#00aeef")
blue_team_score.grid(row=1,column=0)

timer_fr = Frame(centre_fr, bg="#FFFFFF", width=400, height = 400)
timer_fr.grid(row=0,column=1)

red_team_fr = Frame(centre_fr,bg="#ba014e", width=400, height=400)
red_team_fr.grid(row=0,column=2)


root.mainloop()