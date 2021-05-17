import sqlite3 as sql

def sql_query(db_file,command):
    # connect to database
    with sql.connect(db_file) as db:
        cursor = db.cursor()

        # run the command
        cursor.execute(command)
        return cursor.fetchall()

# ----- MAIN PROGRAM -----
DB_FILE = "./IA2/spotify_v2.db"

query = """
        SELECT *
        FROM Songs
        """

results = sql_query(DB_FILE,query)
for row in results:
    print(row)