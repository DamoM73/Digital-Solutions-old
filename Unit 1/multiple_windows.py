import tkinter as tk

root = tk.Tk()
time = tk.IntVar()
time.set(0)

def change_label():
    entry_window = tk.Toplevel()
    entry = tk.Entry(entry_window)
    entry.pack()

    def submit(entry):
        time.set(entry.get())
        label.config(text=str(time.get()))
        root.update()
        entry_window.destroy()

    tk.Button = tk.Button(entry_window,text="Submit", command= lambda: submit(entry)).pack()

label = tk.Label(root, text=str(time.get()))
label.pack()
tk.Button(root,text="Change", command=change_label).pack()

root.mainloop()