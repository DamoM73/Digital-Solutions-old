import sqlite3 as sql
import csv
import os

def delete_db(db_file):
    if os.path.exists(db_file):
        os.remove(db_file)

def sql_command(db_file,command):
    # connect to database
    with sql.connect(db_file) as db:
        cursor = db.cursor()

        # run the command
        cursor.execute(command)

def sql_query(db_file, query):
    # connect to database
    with sql.connect(db_file, query) as db:
        cursor = db.cursor()

        # run query
        cursor.execute(query)
        return cursor.fetchall()

def create_db(db_file):
    # artist table
    create_artist_tbl = """
                    CREATE TABLE Artist (
                        artist_id TEXT PRIMARY KEY,
                        artist_name TEXT NOT NULL
                    );
                    """
    sql_command(db_file, create_artist_tbl)

    # genre table
    create_genre_tble = """
                        CREATE TABLE Genre (
                            genre_id INTEGER PRIMARY KEY,
                            genre_name TEXT NOT NULL
                        );
                        """
    sql_command(db_file, create_genre_tble)
    

    # artist/genre table
    create_artistgenre_tbl = """
                            CREATE TABLE Artist_Genre (
                                artist_id TEXT NOT NULL REFERENCES Artist(artist_id),
                                genre_id TEXT NOT NULL REFERENCES Genre (genre_id),
                                PRIMARY KEY (artist_id, genre_id)                           
                            );
                            """
    sql_command(db_file, create_artistgenre_tbl)

    # song table
    create_song_tbl = """
                        CREATE TABLE Songs (
                            song_id TEXT PRIMARY KEY,
                            song_name TEXT,
                            popularity INTEGER NOT NULL,
                            duration INTEGER NOT NULL,
                            explict INTERGER NOT NULL,
                            danceability REAL NOT NULL,
                            valence REAL NOT NULL,
                            year INTEGER NOT NULL,
                            accousticness REAL NOT NULL,
                            energy REAL NOT NULL,
                            instrumentalness REAL NOT NULL,
                            key INTEGER NOT NULL,
                            liveness REAL NOT NULL,
                            loudness REAL NOT NULL,
                            mode INTEGER NOT NULL,
                            speechiness REAL NOT NULL,
                            tempo REAL NOT NULL
                        );
                        """
    sql_command(db_file,create_song_tbl)

    # song/artist table
    create_songartist_tbl = """
                            CREATE TABLE Song_Artist (
                                song_id TEXT NOT NULL REFERENCES Song(song_id),
                                artist_id TEXT NOT NULL REFERENCES Artist(artist_id),
                                PRIMARY KEY (song_id,artist_id)
                            );
                            """
    sql_command(db_file,create_songartist_tbl)

def import_db(db_file):
    # import artist data and genre data
    with open(ARTIST_FILE, encoding="utf-8") as csv_file:
        csv_reader = csv.reader(csv_file, delimiter = ",")
        next(csv_reader)    # skips header
        # create sql command for each row / record
        added_genres = []
        for row in csv_reader:
            # add artist information
            id = row[0]
            name = row[3].replace('"',"'")
            insert_artist = f"""
                            INSERT INTO Artist (artist_id, artist_name)
                            VALUES ("{id}","{name}")
                            """
            sql_command(db_file,insert_artist)
            print(f"Artist {name} added")

            # add genre information
            genres = row[2].strip('][').split(',')
            for raw_genre in genres:
                genre = raw_genre.strip()[1:-1]
                if genre not in added_genres and genre != "":
                    insert_genre = f"""
                                    INSERT INTO Genre (genre_name)
                                    VALUES ("{genre}")
                                    """
                    sql_command(db_file,insert_genre)
                    added_genres.append(genre)
                    print(f"Genre of {genre} added")
    
    # import song data
    with open(DATA_FILE, encoding="utf-8") as csv_file:
        csv_reader = csv.reader(csv_file, delimiter = ",")
        next(csv_reader)    # skips header
        # create sql command for each row / record
        for row in csv_reader:
            id = row[8]
            name = row[14].replace('"',"'")
            pop = row[15]
            duration = row[5]
            explict = row[7]
            dance = row[4]
            vale = row[0]
            year = row[1]
            accoustic = row[2]
            energy = row[6]
            instrument = row[9]
            key = row[10]
            live = row[11]
            loud = row[12]
            mode = row[13]
            speech = row[17]
            tempo = row[18]
            
            insert_songs = f"""
                            INSERT INTO Songs
                            VALUES ("{id}","{name}",{pop},{duration},{explict},{dance},{vale},
                            {year},{accoustic},{energy},{instrument},{key},{live},{loud},{mode},{speech},{tempo})
                            """
                
            sql_command(db_file,insert_songs)
            print(f"Song {name} added")
            





# ----- MAIN PROGRAM -----
DB_FILE = "./IA2/spotify.db"
ARTIST_FILE = "./IA2/artists.csv"
DATA_FILE = "./IA2/data_o.csv"

delete_db(DB_FILE)
create_db(DB_FILE)
import_db(DB_FILE)