import psycopg2

# connect database
connection = psycopg2.connect(database="chinook")

# create cursor
cursor = connection.cursor()

# Query 1 Artist records
#cursor.execute('SELECT * FROM "Artist"')

# Query 2 Artists name records
# cursor.execute('SELECT "Name" FROM "Artist"')

# Query  3 only Queen from artists records
# cursor.execute('SELECT * FROM "Artist" WHERE "Name" = %s', ["Queen"])

# Query 4 artistid 51 from artists records
# cursor.execute('SELECT * FROM "Artist" WHERE "ArtistId" = %s', [51])

# Query 5 album records from artistid 51
# cursor.execute('SELECT * FROM "Album" WHERE "ArtistId" = %s', [51])

# Query 6 tracks from albumid 51 artist records
cursor.execute('SELECT * FROM "Track" WHERE "Composer" = %s', ["Queen"]) 

# fetch multipul results
results = cursor.fetchall()

# fetch single result
# results = cursor.fetchone()

# closr the connection
connection.close()

# print results
for result in results:
    print(result) 