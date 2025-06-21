from sqlslchemy import (
    create_engine, Column, Float, ForeignKey, Integer, String, 
)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker 


# instructions for chinook database
db = create_engine("postgresql:///chinook")
Base = declarative_base()


# create class-based model for Artist table
class Artist(Base):
    __tablename__ = "Artist"
    ArtistId = Column(Integer, primary_key=True)
    Name = Column(String)


# create class-based model for Album table
class Album(Base):
    __tablename__ = "Album"
    AlbumId = Column(Integer, primary_key=True)
    Title = Column(String)
    ArtistId = Column(Integer, ForeignKey("Artist.ArtistId"))


# create class-based model for Track table
class Track(Base):
    __tablename__ = "Track"
    TrackId = Column(Integer, primary_key=True)
    Name = Column(String)
    AlbumId = Column(Integer, ForeignKey("Album.AlbumId"))
    MediaTypeId = Column(Integer, primary_key=False)
    GenreId = Column(Integer, primary_key=False)
    Composer = Column(String)
    Milliseconds = Column(Integer, primary_key=False)
    Bytes = Column(Integer, primary_key=False)
    UnitPrice = Column(Float)


# connect to a session instead of database
# create a session
session = sessionmaker(db)
# opens a session
session = session()

# create subclass for database
base.metadata.create_all(db)


# Query 1 all Artist records
# artist = session.query(Artist)
# for artist in artists:
#    print(artist.ArtistId, artist.name, sep=" | ")

# Query 2 only Artist names
# artists = session.query(Artist)
# for artist in artists:
#    print(artist.Name)

# Query 3 only Queen from artists records
# artist = session.query(Artist).filter(Artist.Name == "Queen").first()
# print(artist.ArtistId, artist.Name, sep=" | ")

# Query 4 artistid 51 from artists records
# artist = session.query(Artist).filter_by(ArtistId=51).first()
# print(artist.ArtistId, artist.Name, sep=" | ")

# Query 5 album records from artistid 51
# albums = session.query(Album).filter_by(ArtistId=51)
# for album in albums:
#    print(album.AlbumId, album.Title, album.ArtistId, sep=" | ")

# Query 6 tracks from composer is Queen from artist records
tracks = session.query(Track).filter_by(Composer="Queen")
for track in tracks:
    print(
        track.TrackId, 
        track.Name,
        track.AlbumId,
        track.MediaTypeId,
        track.GenreId,
        track.Composer,
        track.Milliseconds,
        track.Bytes,
        track.UnitPrice,
        sep=" | "
    )
    