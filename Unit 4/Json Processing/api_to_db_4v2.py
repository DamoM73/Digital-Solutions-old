from sqlite3.dbapi2 import Cursor
import requests
import json
import sqlite3

DB_FILE = "./Unit 4/Json Processing/food_trucks.db"

def jprint(obj):
    if obj.status_code == 200:
        print(json.dumps(obj.json(), indent=4))
    else:
        print(obj.status_code, "error in retrieving API")

def create_table(filename, tablename, sqlcommand):
    # connect to database file
    with sqlite3.connect(filename) as database:
        cursor = database.cursor()
        
        # remove previous table
        cursor.execute(f"DROP TABLE IF EXISTS {tablename}")

        # create empty table
        cursor.execute(sqlcommand)

def table_insert(db_file,command,values):
    # connect to database file
    with sqlite3.connect(db_file) as database:
        cursor = database.cursor()

        cursor.executemany(command,values)
        


# ---- MAIN PROGRAM -----
# -- retrieve data from API --
trucks_data = requests.get("https://www.bnefoodtrucks.com.au/api/1/trucks")

#jprint(trucks_data)

# -- create database tables --
create_truck_table = """
                        CREATE TABLE Trucks (
                            truck_id INTEGER PRIMARY KEY,
                            name TEXT NOT NULL,
                            category TEXT NOT NULL,
                            website TEXT);
                        """

create_table(DB_FILE, "Trucks", create_truck_table)

# sites table
create_sites_tbl = """
                    CREATE TABLE Sites (
	                    site_id INTEGER PRIMARY KEY,
	                    street TEXT NOT NULL,
	                    suburb TEXT NOT NULL,
	                    postcode INTEGER NOT NULL,
	                    latitude REAL,
	                    longitude REAL);
                    """
create_table(DB_FILE,"Sites",create_sites_tbl)

# bookings table
create_bookings_tble = """
                        CREATE TABLE Bookings (
                            	booking_id INTEGER PRIMARY KEY,
                                site_id INTEGER NOT NULL,
                                truck_id INTEGER NOT NULL,
                                date TEXT, 
                                start TEXT,
                                finish TEXT);
                        """
create_table(DB_FILE,"Bookings",create_bookings_tble)

values = []
for row in trucks_data.json():
    truck_id = row['truck_id']
    name = row['name']
    category = row['category']
    if row['website'] == '':
        website = 'none'
    else:
        website = row['website']

    values.append((truck_id,f"{name}",f"{category}",f"{website}"))
print(values)
truck_insert = "INSERT INTO Trucks VALUES (?,?,?,?)"

table_insert(DB_FILE,truck_insert,values)