import sqlite3
import os

PATH = "/GIT/Digital-Solutions/Unit 3/CSV_import/"
DB_FILE = PATH + "fitness.db"

def create_table(sql_command):
    # create a table within the database
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
    create_table(classes_table)

    # create sexes table
    sexes_table = """
                    CREATE TABLE Sexes (
                        sex TEXT PRIMARY KEY,
                        sex_name TEXT NOT NULL
                    );
                    """
    create_table(sexes_table)


    # create Weight table
    weight_table = """
                    CREATE TABLE Weight (
                        height INTEGER PRIMARY KEY,
                        max_weight INTEGER NOT NULL,
                        min_weight INTEGER NOT NULL
                    );
                    """
    create_table(weight_table)

    # create Clients table
    clients_table = """
                    CREATE TABLE Clients (
                        id_number INTEGER PRIMARY KEY,
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
    create_table(clients_table)

    # create readings table
    readings_table = """
                    CREATE TABLE Readings (
                        id_number INTERGER NOT NULL,
                        month TEXT NOT NULL,
                        RHR INTEGER NOT NULL,
                        weight INTEGER NOT NULL,
                        PRIMARY KEY(id_number,month)
                    );
                    """
    create_table(readings_table)

def import_csv():
    # extreacts the data from provided CVS files and enters into the database
    pass

def query_db():
    # runs the given query on the database
    pass

def export_csv():
    # saves the proved data to csv file
    pass

# ===== MAIN PROGRAM =====
if not os.path.exists(DB_FILE):
    create_database()