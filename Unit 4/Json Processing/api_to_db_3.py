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