import csv

library_db = []

with open('./Unit 3/Library.txt') as library_file:
    csv_reader = csv.reader(library_file, delimiter='\t')
    line_count = 0
    for item in csv_reader:
        # print(item)
        # item = list(item.split('\t'))   
        # isbn = item[10]
        # title = item[21].strip('"')
        # book = item[26] == 'Monograph'
        author = item[32].strip('"')
        
        print(author)

        # if book:
        #     library_db.append([isbn,author,title,])
    
# for book in library_db:
#     print(book)

