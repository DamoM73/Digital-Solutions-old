# prime number exercise part 1

# get candidate number from user
num = False
while not num:
    candidate = input("Enter a number to check if prime: ")
    try:                            # execute the command below
        candidate = int(candidate)
    except:                         # if it raises an error execute the block below
        candidate = input("Enter a number to check if prime: ")
    else:                           # if it doesn't raise an error, execute the block below`
        num = True


# check if candiadate is prime number
prime = True
dividend = 2

while prime:                            # same as while prime == True:
    if candidate % dividend == 0:
        print(f"{candidate} is a non-prime")
        prime = False
    elif dividend == candidate - 1:
        print(f"{candidate} is a prime")
        break
    else:
        dividend += 1