import sqlite3

with sqlite3.connect("./Unit 2/movies.db") as db:
    cursor = db.cursor()
    cursor.execute("""
        SELECT dirname
        FROM director
        WHERE country = :country
        """,
        {'country': "US"})

    results = cursor.fetchall()

    print(results)