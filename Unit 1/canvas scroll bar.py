from tkinter import *

# **** Create Window ****
root = Tk()

# **** Window Content

# create scrollbar
vscrollbar = Scrollbar(root)
vscrollbar.pack(side=RIGHT, fill=Y) 

# create canvas to be scrolled
base_canvas= Canvas(root,yscrollcommand=vscrollbar.set)
base_canvas.pack(side=RIGHT, fill="both", expand=True)

# assign scrollbar command to adjust verticle view of canvas
vscrollbar.config(command=base_canvas.yview)

# make frame to contain widgets
widget_frame = Frame(base_canvas)


# create a tkinter wideget on a canvase (create_window)
base_canvas.create_window(0,0,window=widget_frame, anchor='nw')

# add content
for i in range(100):
    Label(widget_frame,wraplength=350 ,text=r"Det er en kendsgerning, at man bliver distraheret af læsbart indhold på en side, når man betragter dens websider, som stadig er på udviklingsstadiet. Der har været et utal af websider, som stadig er på udviklingsstadiet. Der har været et utal af variationer, som er opstået enten på grund af fejl og andre gange med vilje (som blandt andet et resultat af humor).").pack()
    Button(widget_frame,text="anytext").pack()

# update the screen before calculating the scrollregion
root.update()

# limit scroll region to the height of the canvas
base_canvas.config(scrollregion=base_canvas.bbox(ALL))


# **** run window loop ****
root.mainloop()