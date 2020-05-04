import requests
import json
import sqlite3
import csv

DB_FILE = "./Unit 3/library_catalogue.db"

def create_table(filename, tablename, sqlcommand):
    # connect to database file (will create it if not existing)
    with sqlite3.connect(filename) as database:
        cursor = database.cursor()
        
        # remove previous table and data
        cursor.execute(f"DROP TABLE IF EXISTS {tablename};")

        # create empty table
        cursor.execute(sqlcommand)

def table_insert(db_file, table_name, values):
    # connect to database file
    with sqlite3.connect(db_file) as database:
        cursor = database.cursor()

        # execute an insert statement for each row of provided data list
        records = 0
        for row in values:
            # print(row)
            cursor.execute(f"""
                            INSERT INTO {table_name}
                            VALUES ({row});
                            """)
            records += 1
            print(f"Added {records} records to the {table_name} table")

# ---- MAIN PROGRAM ----

# -- create database tables --
create_catalogue_tbl = """
                    CREATE TABLE Catalogue (
                        BookID INTEGER,
                        Title TEXT NOT NULL,
                        Author TEXT NOT NULL,
                        Abstract TEXT NOT NULL,
                        Section TEXT NOT NULL,
                        Length TEXT NOT NULL,
                        ISBN TEXT NOT NULL,
                        Read_level TEXT NOT NULL,
                        Read_flag BOOLEAN NOT NULL);
                    """
create_table(DB_FILE,"Catalogue",create_catalogue_tbl)

# -- insert values database tables --
# open library file
with open('./Unit 3/Library.txt') as library_db:
    # parse TSV file
    csv_reader = csv.reader(library_db, delimiter = '\t')
    # iterate over the books in the library database
    values = []
    for row in csv_reader:
        # get values of each book
        BookID = row[1]
        Title = row[21]
        Author = row[32]
        Abstract = ""
        Section = row[3]
        Length = row[4]
        ISBN = row[10]
        Read_level = "Junior"
        Read_flag = 0
        values.append(f'{BookID}, "{Title}", "{Author}", "{Abstract}", "{Section}", "{Length}", "{ISBN}", "{Read_level}", "{Read_flag}"')
    table_insert(DB_FILE,"Catalogue", values)
      