def bubbleSort(values):
        
    for pass_num in range(len(values)):
               
        for pointer in range(len(values) - 1 - pass_num):
            if values[pointer] > values[pointer +1]:
                values[pointer], values[pointer + 1] = values[pointer + 1], values[pointer]
            
    
    return(values)

example_list = [19,10,8,17,9]
sorted_list = bubbleSort(example_list)
print(sorted_list)