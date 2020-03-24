from tkinter import *


def nxt():
    global index 
    index += 1
    if index > len(frame_list)-1:
        index = 0
    frame_update()      

def prev():
    global index
    index -= 1
    if index < 0:
        index = len(frame_list)-1
    frame_update()

def frame_update():
    frame_list[index].tkraise()  
    root.update()

index = 0
frame_list = []

root = Tk()

button_frame = Frame(width=300)
button_frame.grid(row=0,column=0)

Button(button_frame,text="Next", command=nxt).grid(row=0, column=1)
Button(button_frame, text="Previous", command=prev).grid(row=0, column=0)

policy_frame = Frame(height=10)
policy_frame.grid(row=1, column=0)

first_frame = LabelFrame(policy_frame, text="First")
Label(first_frame, text="First", width=100).grid(row=0,column=0)
first_frame.grid(row=0, column=0)
frame_list.append(first_frame)

second_frame = LabelFrame(policy_frame, text="Second")
Label(second_frame,text="Second", width=100).grid(row=0, column=0)
frame_list.append(second_frame)
second_frame.grid(row=0, column=0)

third_frame = LabelFrame(policy_frame, text="Third")
Label(third_frame,text="Third", width=100).grid(row=0, column=0)
frame_list.append(third_frame)
third_frame.grid(row=0, column=0)

frame_update()

print(frame_list)

#frame_list[index].grid(row=0, column=0)

root.mainloop()