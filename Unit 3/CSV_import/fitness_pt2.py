import sqlite3
import os
import csv

PATH = "/GIT/Digital-Solutions/Unit 3/CSV_import/"
DB_FILE = PATH + "fitness.db"

def sql_command(sql_command):
    # run the sql command on the database
    with sqlite3.connect(DB_FILE) as database:
        cursor = database.cursor()

        cursor.execute(sql_command)

def create_database():
    # create classes table
    classes_table = """
                    CREATE TABLE Classes (
                        activity TEXT PRIMARY KEY,
                        instructor TEXT NOT NULL,
                        max_size INTEGER NOT NULL
                    );
                    """
    sql_command(classes_table)

    # create sexes table
    sexes_table = """
                    CREATE TABLE Sexes (
                        sex TEXT PRIMARY KEY,
                        sex_name TEXT NOT NULL
                    );
                    """
    sql_command(sexes_table)


    # create Weight table
    weight_table = """
                    CREATE TABLE Weight (
                        height INTEGER PRIMARY KEY,
                        max_weight INTEGER NOT NULL,
                        min_weight INTEGER NOT NULL
                    );
                    """
    sql_command(weight_table)

    # create Clients table
    clients_table = """
                    CREATE TABLE Clients (
                        id_number TEXT PRIMARY KEY,
                        name TEXT NOT NULL,
                        street TEXT NOT NULL,
                        town TEXT NOT NULL,
                        age INTEGER NOT NULL,
                        activity TEXT NOT NULL,
                        sex TEXT NOT NULL,
                        height INTEGER NOT NULL,
                        FOREIGN KEY (activity) 
                            REFERENCES Classes (activity)
                        FOREIGN KEY (sex)
                            REFERENCES Sexes (sex)
                        FOREIGN KEY (height)
                            REFERENCES Weight (height)
                    );
                    """
    sql_command(clients_table)

    # create readings table
    readings_table = """
                    CREATE TABLE Readings (
                        id_number TEXT NOT NULL,
                        month TEXT NOT NULL,
                        RHR INTEGER NOT NULL,
                        weight INTEGER NOT NULL,
                        PRIMARY KEY(id_number,month)
                    );
                    """
    sql_command(readings_table)

def process_record(record):
    new_record = ""
    for item in record:
        if item.isdigit():
            new_record = new_record + item + ","
        else:
            new_record = new_record + "'" + item + "',"
    return new_record[:-1]

def parse_csv(file_name, table):
    # open the add each line of csv file as a new record in the db table
    with open(file_name) as csv_file, sqlite3.connect(DB_FILE) as database:
        # connect to db
        cursor = database.cursor()
        # read from csv file       
        csv_reader = csv.reader(csv_file, delimiter = ",")
        for row in csv_reader:
            values = process_record(row)
            insert_values = f"""
                            INSERT INTO {table}
                            VALUES ({values})
                            """
            sql_command(insert_values)

def import_csv():
    # parse classes table
    parse_csv(PATH + "tblClasses.csv","Classes")
    parse_csv(PATH + "tblSexes.csv", "Sexes")
    parse_csv(PATH + "tblWeight_Chart.csv", "Weight")
    parse_csv(PATH + "tblClients.csv", "Clients")
    parse_csv(PATH + "tblReadings.csv", "Readings")

def query_db():
    # runs the given query on the database
    pass

def export_csv():
    # saves the proved data to csv file
    pass

# ===== MAIN PROGRAM =====
if not os.path.exists(DB_FILE):
    create_database()
    import_csv()