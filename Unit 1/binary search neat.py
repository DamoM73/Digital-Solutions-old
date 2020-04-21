find = 13
found = False
num_list = [1,3,4,5,7,9,11,14,16]
length = len(num_list)
lower_bound = 0
upper_bound = length

while not found:
    midpoint = (upper_bound + lower_bound) // 2
    print(lower_bound,midpoint,upper_bound)
    if num_list[midpoint] == find:
        print("Found at", midpoint)
        found = True
    elif num_list[midpoint] > find:
        upper_bound = midpoint - 1
    elif num_list[midpoint] < find:
        lower_bound = midpoint + 1
    
    if upper_bound < lower_bound:
        print("Not found")
        break
