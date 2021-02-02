import csv

# open csv file to example_file variable
with open('./Unit 3/example.csv') as example_file:
    # create object to read file
    example_reader = csv.reader(example_file)
    
    # convert file content to list
    example_data = list(example_reader)

# display to terminal
print(example_data)