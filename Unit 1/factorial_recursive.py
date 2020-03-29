def get_factorial(num):
    if num < 2:
        return 1
    else:
        return num * get_factorial(num-1)


print(get_factorial(100))