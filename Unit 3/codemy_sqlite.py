from tkinter import *
from PIL import ImageTk, Image
import sqlite3

root = Tk()
root.title('Codemy SQLite tutorial')
root.geometry("400x400")

# Databases

# create or connect to database
conn = sqlite3.connect('address_book.db')

# create cursor
c = conn.cursor()

# create table
'''
c.execute("""CREATE TABLE addresses (
    first_name text,
    last_name text,
    address text,
    city text,
    state text,
    postcode integer
    )""")
'''
# Create a function to Delete a Record
def delete():
    # connect to database
    conn = sqlite3.connect('address_book.db')
    # create cursor
    c = conn.cursor()

    # Delete a record
    c.execute("DELETE FROM addresses WHERE oid = "+ delete_box.get())

    # commit changes
    conn.commit()
    # close connection
    conn.close()


# Create submit function for database
def submit():
    # connect to database
    conn = sqlite3.connect('address_book.db')
    # create cursor
    c = conn.cursor()

    #print(f"{f_name.get()},{l_name.get()},{address.get()},{city.get()},{state.get()},{pcode.get()}")

    # insert into table
    c.execute(f"INSERT INTO addresses VALUES ('{f_name.get()}','{l_name.get()}','{address.get()}','{city.get()}','{state.get()}',{pcode.get()})")


    # commit changes
    conn.commit()

    # close connection
    conn.close()

    # Clear the text boxes
    f_name.delete(0, END)
    l_name.delete(0, END)
    address.delete(0, END)
    city.delete(0, END)
    state.delete(0, END)
    pcode.delete(0, END)

# Create query function
def query():
    # connect to database
    conn = sqlite3.connect('address_book.db')
    # create cursor
    c = conn.cursor()

    c.execute("SELECT *, oid FROM addresses")
    records = c.fetchall()
    #print(records)
    print_records = ""
    for record in records:
        print_records += record[0] + " " + record[1] + " " + str(record[6]) + "\n"
    
    query_lb = Label(root, text=print_records)
    query_lb.grid(row=10,column=0,columnspan=2)

    # commit changes
    conn.commit()
    # close connection
    conn.close()


# Create text boxes
f_name = Entry(root, width=30)
f_name.grid(row=0,column=1, padx=20, pady=(10,0))
l_name = Entry(root, width=30)
l_name.grid(row=1,column=1, padx=20)
address = Entry(root, width=30)
address.grid(row=2,column=1, padx=20)
city = Entry(root, width=30)
city.grid(row=3,column=1, padx=20)
state = Entry(root, width=30)
state.grid(row=4,column=1, padx=20)
pcode = Entry(root, width=30)
pcode.grid(row=5,column=1, padx=20)
delete_box = Entry(root, width=30)
delete_box.grid(row=7,column=1, padx=20)

# Create text box labels
Label(root, text="First name").grid(row=0,column=0, pady=(10,0))
Label(root, text="Last name").grid(row=1,column=0)
Label(root, text="Address").grid(row=2,column=0)
Label(root, text="City").grid(row=3,column=0)
Label(root, text="State").grid(row=4,column=0)
Label(root, text="Post Code").grid(row=5,column=0)
Label(root, text="Delete ID").grid(row=7,column=0)

# Create Submit button
submit_btn = Button(root, text="Add record to database", command=submit)
submit_btn.grid(row=6,column=0,columnspan=2,pady=10, padx=10, ipadx=100)

# Create Query button
query_btn = Button(root, text="Show Records", command=query)
query_btn.grid(row=9,column=0,columnspan=2,pady=10, padx=10, ipadx=125)

# Create a delete button
delete_btn = Button(root, text="Delete Record", command=delete)
delete_btn.grid(row=8,column=0,columnspan=2,pady=10, padx=10, ipadx=125)

# commit changes
conn.commit()

# close connection
conn.close()

root.mainloop()