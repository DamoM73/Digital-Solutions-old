import csv

with open('./Unit 3/output.csv','w',newline='') as output_file:
    output_writer = csv.writer(output_file)
    output_writer.writerow(['spam','eggs','bacon','ham'])
    output_writer.writerow(['Hello, world', 'eggs', 'bacon', 'ham'])
    output_writer.writerow([1,2,3.141592,4])

