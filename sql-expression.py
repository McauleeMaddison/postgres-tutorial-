from sqlalchemy import (
    create_engine, Table, Column, Float, ForeignKey, Integer, String, MetaData,
    )

# execute localhost chinook (db) "database"
db = create_engine("postgresql:///cinook")

meta = MetaDate(db)

# create variable for artist table
artist_table = Table(
    "Artist", meta,
    Column("ArtistId", Integer, primary_key=True),
    Column("Name", String)
)

# create variable for album table
album_table = table(
    "Album", meta,
    Column("AlbumId", Integer, primary_key=True),
    Column("Title", String),
    Column("ArtistId", Integer, ForeignKey("artist_table.ArtistId"))
)

# create variable for track table
track_table = Table(
    "Track", meta,
    Column("TrackId", Integer, primary_key=True),
    Column("Name", String),
    Column("AlbumId", Integer, ForeignKey("album_table.AlbumId"))
    Column("MediaTypeId", Integer, primary_key=False),
    Column("GenreId", Integer, primary_key=False),
    Column("Composer", String),
    Column("Milliseconds", Integer),
    Column("Bytes", Integer),
    Column("UnitPrice", Float)
)

# making the connection
with db.connect() as connection:
    
    # Query 1 all Artist records
    # select_artist = artist_table.select()

    # Query 2 only Artist names
    # select_query = artist_table.select().with_only_columns([artist_table.c.Name])

    # Query 3 only Queen from artists records
    # select_query = artist_table.select().where(artist_table.c.Name == "Queen")

    # Query 4 artistid 51 from artists records
    # select_query = artist_table.select().where(artist_table.c.ArtistId == 51)

    # Query 5 album records from artistid 51
    # select_query = album_table.select().where(album_table.c.ArtistId == 51)
    
    # Query 6 tracks from composer is Queen from artist records
    select_query = track_table.select().where(track_table.c.Composer == "Queen")
    
    results = connection.execute(select_query)
    for result in results:
        print(result)