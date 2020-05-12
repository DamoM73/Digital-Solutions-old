import requests
import xml.etree.ElementTree as ET
import csv

def get_rating(target_isbn):
    # retrieve data from Goodreads' API
    key = "p5vNyMszw7OCDKXJb8EZ8g"
    goodread_api = requests.get("https://www.goodreads.com/book/isbn/" + target_isbn + "?key=" + key)
    
    # will only proceed if there is a successful request (ie. book is in Goodreads' database)
    if goodread_api.status_code == 200:
        # parse XML response
        root = ET.fromstring(goodread_api.content)

        # assigning relevent information to variables
        title = (root[1][1].text)
        avg_rating = (root[1][18].text)

        # printing rating average
        print(f"{title}:\tAverage rating is {avg_rating}")
    else:
        # message if book is not in Goodreads' database 
        print("Not in Goodread database")

# ===== MAIN PROGRAM =====
# open library file
with open('./Unit 3/Library.txt') as library_db:
    # parse TSV file
    csv_reader = csv.reader(library_db, delimiter = '\t')
    # iterate over the books in the library database
    for book in csv_reader:
        # get rating of each book
        #get_rating(book[10])
        print(book[21], book[10])

