import tkinter as tk
from tkinter import Frame, font

FONT = ("Arial",50)

root = tk.Tk()
#root.geometry("600x400")

blue_team_fr = tk.Frame(root)
blue_team_fr.grid(row=0,column=0)
tk.Label(blue_team_fr,text="Box 1",bg="blue",font=FONT).grid(row=0,column=0)
tk.Label(blue_team_fr,text="Box 2",bg="blue",font=FONT).grid(row=1,column=0)

timer_fr = tk.Frame(root)
timer_fr.grid(row=0,column=1)
tk.Label(timer_fr,text="Box 1",bg="white",font=FONT).grid(row=0,column=0)
timer_btn_fr = Frame(timer_fr)
timer_btn_fr.grid(row=1,column=0)
tk.Label(timer_btn_fr,text="Box 2",bg="white",font=FONT).grid(row=0,column=0)
tk.Label(timer_btn_fr,text="Box 3",bg="white",font=FONT).grid(row=0,column=1)

red_team_fr = tk.Frame(root)
red_team_fr.grid(row=0,column=2)
tk.Label(red_team_fr,text="Box 1", bg="red",font=FONT).grid(row=0,column=0)
tk.Label(red_team_fr,text="Box 2", bg="red",font=FONT).grid(row=1,column=0)

root.mainloop()