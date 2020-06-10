from tkinter import *
import time
import winsound

root=Tk()

t1_score = 0

root.title("vewing score board")

root.state("zoomed")

frequency = 1000    # Set Frequency To 2500 Hertz
duration = 1000     # Set Duration To 1000 ms == 1 second
frequency_1 = 1000  
duration_1 = 4000

stopwatch = 0

name_1 = str("")

global point_value_1
global point_value_2
global point_value_3
global round_entrybox
global team_two_entrybox
global timer_one
global timer_one_entrybox
global abc
global counter_down
global round_entrybox


def timer():
    global counter_down
    counter_down = int(abc[0])
    print(abc[0])
    if int(counter_down) >= 0 and running == True:
        timer_one.config(text=counter_down)
        root.update()
        print(counter_down)
        counter_down= int(abc[0])-1
        root.after(1000,timer)
        if counter_down == (-1):
            winsound.Beep(frequency_1, duration_1)
def start_button():
    global running
    running = True
    timer()
    #winsound.Beep(frequency, duration)
    #winsound.Beep(frequency, duration)
    #winsound.Beep(frequency, duration)
def stop():
    global running
    running = False
def reset():
    global running
    global counter_down
    global abc 
    running = False
    #global timer_one_entrybox
    timer_one.config(text=abc[0])
    counter_down = abc[0]
    timer_1()


#----------------------------------------------------functions----------------------------------------------------

#def team_name_1():
   # global team_one_entrybox
    #global name_1
   # global team_one_name
    #name_1 = int(team_one_entrybox.get())
    #team_one_name.config(text=str(name_1))
    #root.update()

#-------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------set up window-----------------------------------------

def ui_button():
    user_input_box=Toplevel(root)
    user_input_box.title("Setup screen")
    user_input_box.geometry("500x400")


    timer_title=Label(user_input_box, text="stopwatch value", font=("20"))
    timer_title.pack()

    global timer_one_entrybox
    

    timer_one_entrybox=Entry(user_input_box)
    timer_one_entrybox.pack()


    #timer_one_button=Button(user_input_box, text="input time", command=stopwatch_button)
    #timer_one_button.pack()

 #-------------------------------------team name input (team1)--------------------------------------------

    team_name_title=Label(user_input_box, text="Config team names", font=("20"))
    team_name_title.pack()

    config_team_name_frame=Frame(user_input_box)
    config_team_name_frame.pack()


    config_name_one_frame=Frame(config_team_name_frame)
    config_name_one_frame.grid(row=0, column=0, padx=10, pady=5)

    global team_one_entrybox

    team_one_entrybox=Entry(config_name_one_frame)
    team_one_entrybox.grid()

    #team_one_entrybox=Button(config_name_one_frame, text="input team 1 name", command=team_name_1)
    #team_one_entrybox.grid()

    #---------------------------------------------team name input (team2)

    config_name_two_frame=Frame(config_team_name_frame)
    config_name_two_frame.grid(row=0, column=1, padx=10, pady=5) 

    global team_two_entrybox

    team_two_entrybox=Entry(config_name_two_frame)
    team_two_entrybox.grid()

    #team_two_entrybox=Button(config_name_two_frame, text="input team 2 name")
    #team_two_entrybox.grid()

    #-------------------------------------point value's---------------------------------------------
    point_value_frame=Frame(user_input_box)
    point_value_frame.pack()


    global point_value_one
    global point_value_two
    global point_value_three

    point_value_label=Label(point_value_frame, text="Config of point values", font=("20"))
    point_value_label.pack()

    point_values=Frame(user_input_box)
    point_values.pack()

    point_value_one=Entry(point_values)
    point_value_one.grid(row=0, column=0, padx=5, pady=5)

    #point_value_one=Button(point_values, text="enter first point value")
    #point_value_one.grid(row=1, column=0)

    point_value_two=Entry(point_values)
    point_value_two.grid(row=0, column=1)

    #point_value_two=Button(point_values, text="enter second point value")
    #point_value_two.grid(row=1, column=1)

    point_value_three=Entry(point_values)
    point_value_three.grid(row=0, column=2, padx=5)

    #point_value_three=Button(point_values, text="enter third point value")
    #point_value_three.grid(row=1, column=2)

    #-----------------------------------------------round button---------------------------------------
    round_frame=Frame(user_input_box)
    round_frame.pack()

    global round_entrybox

    round_title=Label(round_frame, text="Round input", font=("20"))
    round_title.grid(row=0, column=0, pady=5)

    round_entrybox=Entry(round_frame)
    round_entrybox.grid(row=1, column=0, pady=5)

    #round_button=Button(round_frame, text="input round")
    #round_button.grid(row=2, column=0)

    Save_button_frame=Frame(user_input_box)
    Save_button_frame.pack()

    save_button=Button(Save_button_frame, text="save", command=save_and_input)
    save_button.pack()

    user_input_box.mainloop()


#-------------------------------------------Button commands and functions---------------------------------------------

#def team_one_name():
    #int(team_one_entrybox.get()) = team_one_input


def stopwatch_button():
    global timer_one_entrybox
    global stopwatch
    stopwatch = int(timer_one_entrybox.get())
    timer_one.config(text = str(stopwatch))
    root.update()

def round_function():
    global round_entrybox
    global round1
    round1 = int(round_entrybox.get())
    round_label_config.config(text=str(round1))
    root.update()


#-----------------------------------------point calculator--------------------------------------------------

def button_function():
    #global sc1
    team_one_score = 0
    global point_value_1
    #new_team_one_score = (team_one_score) + int(sc1)
    #team_one_score.config(text=str(t1_score))
    
    scoreA = int(team_one_score)
    scoreB = int(point_value_1.get())
    total=scoreA+scoreB
    team_one_score.config(text=str(total))
    Toplevel(root).update()
   





def driver_button():
    driver_button_box=Toplevel(root)
    driver_button_box.title("Driver screen")
    driver_button_box.geometry("500x500")

    #---------------------------------stop watch tittle----------------------------------------------

    stopwatch_title_frame=Frame(driver_button_box)
    stopwatch_title_frame.pack()

    stopwatch_title=Label(stopwatch_title_frame, text="Stopwatch buttons", font=("60"))
    stopwatch_title.pack()

    #--------------------------- buttons for the stopwatch----------------------------------------

    btn_frame=Frame(driver_button_box)
    btn_frame.pack()
    btn_start=Button(btn_frame, text="start",command=start_button, bg="green", fg="black", width=4, height=1, font=("2"))
    btn_start.grid(row=0, column=0, padx=10)

    btn_stop=Button(btn_frame, text="stop", command=stop, bg="red", fg="black", width=4, height=1, font=("2"))
    btn_stop.grid(row=0, column=1, padx=10)

    btn_reset=Button(btn_frame, text="reset", command=reset, bg="yellow", fg="black", width=4, height=1, font=("2"))
    btn_reset.grid(row=0, column=2, padx=10)

    #-----------------------------------------team 1 score and score buttons---------------------------------

    team_point_frame=Frame(driver_button_box)
    team_point_frame.pack()


    point_frame_one=Frame(team_point_frame)
    point_frame_one.grid(row=0, column=0)

    team_one_point_label=Label(point_frame_one, text="team 1 points", bg="blue", fg="white")
    team_one_point_label.grid(row=0, column=0, pady=20)

    spacer_frame=Frame(team_point_frame)
    spacer_frame.grid(row=0, column=1, padx=40)

    point_frame_two=Frame(team_point_frame)
    point_frame_two.grid(row=0, column=2)

    team_two_point_label=Label(point_frame_two, text="team 2 points", bg="red", fg="white")
    team_two_point_label.grid(row=0, column=1, pady=20)

    #-------------------------------------team 1 button frame--------------------------------------

    


    #---------------------------------------------------win screen button------------------------------------

    win_screen_button_frame=Frame(driver_button_box)
    win_screen_button_frame.pack()

    Win_button_one_frame=Frame(win_screen_button_frame)
    Win_button_one_frame.grid(row=0, column=0, pady=10, padx=50)

    win_button_two_frame=Frame(win_screen_button_frame)
    win_button_two_frame.grid(row=0, column=1, pady=10, padx=50)

    win_button_one=Button(Win_button_one_frame, text="Team 1 wins!")
    win_button_one.grid()

    win_button_two=Button(win_button_two_frame, text="Team 3 wins!")
    win_button_two.grid()



    driver_button_box.mainloop()
    
    

#---------------------------Start, stop and reset buttons for stopwatch, along with stopwatch-------------
global timer_one

timer_one=Label(root, text=(stopwatch), bg="white", fg="black", font=("arial", "60"))
timer_one.pack()



#------------------------------------------attempt at team name boxes------------------------------

team_name_frame=Frame(root)
team_name_frame.pack()

#global name_1

global team_one_name

global team_name_entrybox

team_one_frame=Frame(team_name_frame)
team_one_frame.grid(row=0, column=0)
team_one_name=Label(team_one_frame, text="team 1", bg="blue", fg="white", width=6, height=3, font=("arial","50"))
team_one_name.grid(row=1, column=0, padx=10)


spacer_frame=Frame(team_name_frame)
spacer_frame.grid(row=0, column=1, padx=200)


team_two_frame=Frame(team_name_frame)
team_two_frame.grid(row=0, column=2)
team_two_name=Label(team_two_frame, text="team 2", bg="red", fg="white", width=6, height=3, font=("arial", "50"))
team_two_name.grid(row=1, column=1, padx=10)

#-----------------------------------------round label----------------------------------------------------
global round_entrybox
global round1

round1 = "4000"

round_label=Label(spacer_frame, text = "Round", font=("arial","35"))
round_label.pack()

round_label_config=Label(spacer_frame, text=(round1), bg="grey", fg="Black", font=("arial", "40"))
round_label_config.pack()


#----------------------------------------team 1 point label---------------------------------------------

team_score_display=Frame(root)
team_score_display.pack()

global team_one_score

team_one_score=Label(team_score_display, text=(total), bg="blue", fg="white", width=5, height=3, font=("arial", "35"))
team_one_score.grid(row=0, column=0, pady=20)

#-----------------------------------------team 2 point label---------------------------------------------

team_two_score=Label(team_score_display, text="'9'", bg="red", fg="white", width=5, height=3, font=("arial", "35"))
team_two_score.grid(row=0, column=2, pady=20)

team_score_spacer_frame=Frame(team_score_display)
team_score_spacer_frame.grid(row=0, column=1, padx=100)

#--------------------------------------------------Buttons-----------------------------------------------------


button_frame_one=Frame(team_score_display)
button_frame_one.grid(row=1, column=0)

team_one_btn1=Button(button_frame_one, text="point 1", command=button_function) 
team_one_btn1.grid(row=1, column=0, padx=5)
team_one_btn2=Button(button_frame_one, text="point 2")
team_one_btn2.grid(row=1, column=1, padx=5)
team_one_btn3=Button(button_frame_one, text="point 3")
team_one_btn3.grid(row=1, column=2, padx=5)

button_spacer_frame=Frame(team_score_display)
button_spacer_frame.grid(row=1, column=1, padx=350)

#-------------------------------------team 2 button frame------------------------------------------
button_frame_two=Frame(team_score_display)
button_frame_two.grid(row=1, column=2)

team_two_btn1=Button(button_frame_two, text="point 1")
team_two_btn1.grid(row=1, column=0, padx=5)
team_two_btn2=Button(button_frame_two, text="point 2")
team_two_btn2.grid(row=1, column=1, padx=5)
team_two_btn3=Button(button_frame_two, text="point 3")
team_two_btn3.grid(row=1, column=2, padx=5)

#---------------------------pop up window for setup window------------------------------------------

user_setup_button=Button(root, text="open user Setup screen", command = ui_button)
user_setup_button.pack()

#-----------------------------------pop up window for driver window--------------------------------

driver_button=Button(root, text="open user Driver screen", command=driver_button)
driver_button.pack()


def save_and_input():
    global abc
    global point_value_1
    global round_entrybox
    #file = open("values.txt", "w")
    with open("values.txt", "w") as file:
        saved_varis_list = [timer_one_entrybox.get(), team_one_entrybox.get(), team_two_entrybox.get(),\
            round_entrybox.get()]
        print(saved_varis_list)
        for x in saved_varis_list:
            file.write(str(x)+",")
    #print("it got to the end")
    with open("values.txt", "r") as file:
        abc = file.read().split(",")
        timer_one.config(text=abc[0])
        team_one_name.config(text=abc[1])
        team_two_name.config(text=abc[2])
        team_one_score.config(text=abc[3])
        round_label_config.config(text=abc[6])
        #sc1 = abc[3]
        root.update()
        print(abc)
root.mainloop()

#point_value_1.get(), point_value_2.get(), point_value_3.get(),