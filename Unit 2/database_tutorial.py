import sqlite3

def director_country(value):
    with sqlite3.connect("./Unit 2/movies.db") as db:
        cursor = db.cursor()
        cursor.execute(
            """
            SELECT dirname
            FROM director
            WHERE country = :country
            """,
            {'country': value})

        return cursor.fetchall()

def directors_not_from(value):
    with sqlite3.connect("./Unit 2/movies.db") as db:
        cursor = db.cursor()
        cursor.execute(
            """
            SELECT dirname, country
            FROM director
            WHERE country != :country
            """,
            {'country': value})

        return cursor.fetchall()

# ---- MAIN PROGRAM ---- #

"""dir_country = input("Which country? ")

directors = director_country(dir_country)
print(directors)
"""

dir_country = input("Directors from not which? ")

directors = directors_not_from(dir_country)
print(directors)