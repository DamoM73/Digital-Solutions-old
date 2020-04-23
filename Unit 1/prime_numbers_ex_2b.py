import tkinter as tk

def is_prime(candidate):
    # accepts an integer and returns True if candidate is prime and False if candidate is not
    prime = True
    dividend = 2
    while prime:
        if candidate % dividend == 0:
            return False
        elif candidate - dividend == 1:
            return True
        else:
            dividend += 1

def find_next_prime(start):
    # starting at the proiivided number, looks for the next prime
    
    # allow for anomolies of 1 & 2
    if start < 3:
        next_num = 3
    else:
        next_num = start + 1

    #find the next prime
    while True:
        if is_prime(next_num):
            return(next_num)
        else:
            next_num += 1

# ----- Create UI -----
root = tk.Tk()
root.geometry("800x600")


# ----- Main Program -----
highest_prime = 0

while True:
    highest_prime = find_next_prime(highest_prime)
    print(highest_prime)