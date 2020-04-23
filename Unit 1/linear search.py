find = 10
found = False
number_list = [3,5,2,9,6,1,8,7]
length = len(number_list)
counter = 0

while found == False and counter < length:
    if number_list[counter] == find:
        found = True
        print("Found at position", counter)
    else:
        counter = counter + 1

if found == False:
    print("Number not in list")