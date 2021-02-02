import csv

# open csv file to example_file variable
with open('./Unit 3/example.csv') as example_file:
    # create object to read file
    example_reader = csv.reader(example_file)
    
    # we can also interate over the reader
    for row in example_reader:
        print("Row " + str(example_reader.line_num)+": "+ str(row))