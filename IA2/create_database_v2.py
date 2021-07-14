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

def sql_many_command(db_file,command,values):
    # connect to database
    with sql.connect(db_file) as db:
        cursor = db.cursor()

        # run the command
        cursor.executemany(command,values)

def sql_query(db_file, query):
    # connect to database
    with sql.connect(db_file) as db:
        cursor = db.cursor()

        # run query
        cursor.execute(query)
        return cursor.fetchall()

def create_db(db_file):
    # artist table
    create_artist_tbl = """
                    CREATE TABLE Artist (
                        artist_name TEXT PRIMARY KEY
                    );
                    """
    sql_command(db_file, create_artist_tbl)

    # genre table
    create_genre_tble = """
                        CREATE TABLE Genre (
                            genre_name TEXT PRIMARY KEY
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
                                artist_id INTEGER NOT NULL REFERENCES Artist(artist_id),
                                PRIMARY KEY (song_id,artist_id)
                            );
                            """
    sql_command(db_file,create_songartist_tbl)

def convert_to_list(raw):
    processed = raw.strip('][').split(',')
    return processed

def import_db(db_file):
    artist_list = []
    artist_genre_list = []
    genre_list = []
    artist_song_list = []
    song_list = []
    
    # Generate data lists
    with open(ARTIST_FILE, encoding="utf-8") as artist_file:
        artist_reader = csv.reader(artist_file, delimiter = ",")
        next(artist_reader)
        for row in artist_reader:
            artist = row[1]
            artist_list.append((artist,))
            
            genres = convert_to_list(row[0])
            for raw_genre in genres:
                genre = raw_genre.strip()[1:-1]
                if genre != "":
                    genre_list.append((genre,))
                    artist_genre_list.append((artist,genre))

    with open(DATA_FILE, encoding="utf-8") as song_file:                
        song_reader = csv.reader(song_file, delimiter=",")
        next(song_reader)
        for row in song_reader:
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
            song_list.append((id,name,pop,duration,explict,dance,vale,year,accoustic,energy,instrument,key,live,loud,mode,speech,tempo))
            
            artists = convert_to_list(row[3])
            for raw_artist in artists:
                artist = raw_artist.strip()[1:-1]
                artist_song_list.append((id,artist))
            

                    
    print(artist_genre_list)        
    # Write data lists to database
    sql_many_command(db_file,"INSERT INTO Artist VALUES (?)",artist_list)
    sql_many_command(db_file,"INSERT OR IGNORE INTO Genre VALUES (?)",genre_list)
    sql_many_command(db_file,"INSERT OR IGNORE INTO Artist_Genre VALUES (?,?)",artist_genre_list)
    sql_many_command(db_file,"INSERT INTO Songs VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)",song_list)
    sql_many_command(db_file,"INSERT OR IGNORE INTO Song_Artist VALUES (?,?)",artist_song_list)




# ----- MAIN PROGRAM -----
DB_FILE = "./IA2/spotify_v2.db"
ARTIST_FILE = "./IA2/data_by_artist_o.csv"
DATA_FILE = "./IA2/data_o.csv"

delete_db(DB_FILE)
create_db(DB_FILE)
import_db(DB_FILE)
#sql_command(DB_FILE,"DROP TABLE Song_Artist")