import tkinter as tk

def display():
    checkvalue = control.get()
    test_label.config(text=str(checkvalue))

root = tk.Tk()

control = tk.IntVar()
test_check = tk.Checkbutton(root,variable=control, command = display)
test_check.pack()

test_label = tk.Label(root, text="")
test_label.pack()

tk.mainloop()