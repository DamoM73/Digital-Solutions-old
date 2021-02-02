import csv

# open csv file to example_file variable
with open('./Unit 3/example.csv') as example_file:
    # create object to read file
    example_reader = csv.reader(example_file)
    
    # convert file content to list
    example_data = list(example_reader)

# since example_data is a list, we can access the elements
print(example_data[0][0])  # this is the first element of the first element, or the first cell in the first row