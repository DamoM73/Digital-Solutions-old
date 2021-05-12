import sqlite3
import csv

def sql_command(command):
    # runs the provided sql command on the data base file store in DATABASE constant
    
    # connect to database
    with sqlite3.connect(DATABASE) as db:
        cursor = db.cursor()

        # run the command
        cursor.execute(command)

def sql_many_command(command,values):
    # runs the provided sql command using the executemany command

    # connect to database
    with sqlite3.connect(DATABASE) as db:
        cursor = db.cursor()

        # run the command
        cursor.executemany(command,values)

def create_db():
    # creates the database tables in the default DATABASE

    # create Cruise table
    cruise_tbl = """
                    CREATE TABLE Cruise (
                        cruise_id TEXT PRIMARY KEY,
                        group_name TEXT NOT NULL,
                        ship_name TEXT NOT NULL
                    )
                    """
    sql_command(cruise_tbl)

    # create the Reading table
    reading_tbl = """
                    CREATE TABLE Reading (
                        date TEXT NOT NULL,
                        time TEXT NOT NULL,
                        lat REAL NOT NULL,
                        long REAL NOT NULL,
                        co2 REAL NOT NULL,
                        sea_temp REAL NOT NULL,
                        salinity REAL NOT NULL, 
                        cruise_id TEXT NOT NULL REFERENCES Cruise(cruise_id),
                        PRIMARY KEY (date,time)
                    )
                    """
    sql_command(reading_tbl)

def enter_data():
    # will enter data from the DATASOURCE file into the DATABASE structure
    
    # create emplty lists for each table
    cruise_list = []
    reading_list = []

    # connect to csv file
    with open(DATASOURCE, encoding="utf-8") as data_file:
        reader = csv.reader(data_file, delimiter=',')

        # advance past the header rows
        next(reader)
        next(reader)

        # read each row of the cvs file and extract required values
        for row in reader:
            # extract Cruise table data
            cruise_id = row[1]
            groupship = row[0]
            # split groupship into atomic values
            group = groupship[:groupship.find("/")]
            ship = groupship[groupship.find("/")+1:]
            # append tuple of values to the cruise list
            cruise_list.append((cruise_id,group,ship))

            # extract Reading table data
            date = row[3]
            time = row[4]
            lat = row[5]
            long = row[6]
            co2 = row[7]
            sea_tmp = row[13]
            salinity = row[14]
            cruise_id = row[1]
            # append tuple of values to the reading list
            reading_list.append((date,time,lat,long,co2,sea_tmp,salinity,cruise_id))

    sql_many_command("INSERT OR IGNORE INTO Cruise VALUES (?,?,?)",cruise_list)
    sql_many_command("INSERT INTO Reading VALUES (?,?,?,?,?,?,?,?)", reading_list)


# ----- MAIN PROGRAM -----
DATABASE = "./Unit 3/csv_import_v2/gbr_data.db"
DATASOURCE = "./Unit 3/csv_import_v2/Great_Barrier_Reef_Dataset_Novice.csv"

create_db()
enter_data()

