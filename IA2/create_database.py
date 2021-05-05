import sqlite3 as sql
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
                            released TEXT NOT NULL,
                            danceability REAL NOT NULL,
                            valence REAL NOT NULL,
                            year INTEGER NOT NULL,
                            accousticness REAL NOT NULL,
                            energy REAL NOT NULL,
                            instrumentalness REAL NOT NULL
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
    # import artist table
    pass

# ----- MAIN PROGRAM -----
DB_FILE = "./IA2/spotify.db"

delete_db(DB_FILE)
create_db(DB_FILE)
import_db(DB_FILE)