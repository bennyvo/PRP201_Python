CREATE TABLE Genre (
	id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
	name TEXT
)

CREATE TABLE Album (
	id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
	artist_id INTEGER,
	title TEXT
)

CREATE TABLE Track (
	id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
	title TEXT,
	album_id INTEGER,
	genre_id INTEGER,
	len INTEGER,
	rating INTEGER,
	count INTEGER
)

INSERT INTO Artist(name) VALUES ('Mozart');
INSERT INTO Artist(name) VALUES ('Trinh Cong Son');
INSERT INTO Artist(name) VALUES ('Michael Jackson');
INSERT INTO Artist(name) VALUES ('Adele');
INSERT INTO Artist(name) VALUES ('Yani');

INSERT INTO Genre(name) VALUES ('Rock');
INSERT INTO Genre(name) VALUES ('RnB');
INSERT INTO Genre(name) VALUES ('Pop');

INSERT INTO Album(title, artist_id) VALUES ('Who Made Who', 2);
INSERT INTO Album(title, artist_id) VALUES ('IV', 1);

insert into Track (title, rating, len, count, album_id, genre_id) 
     values ('Black Dog', 5, 297, 0, 2, 1)
insert into Track (title, rating, len, count, album_id, genre_id)                    
     values ('Stairway', 5, 482, 0, 2, 1)
insert into Track (title, rating, len, count, album_id, genre_id) 
     values ('About to Rock', 5, 313, 0, 1, 2)
insert into Track (title, rating, len, count, album_id, genre_id) 
     values ('Who Made Who', 5, 207, 0, 1, 2)

select Album.title, Artist.name from Album join Artist on Album.artist_id = Artist.id
select Album.title, Album.artist_id, Artist.id,Artist.name from Album join Artist on Album.artist_id = Artist.id
SELECT Track.title, Track.genre_id, Genre.id, Genre.name FROM Track JOIN Genre   
select Track.title, Genre.name from Track join Genre on Track.genre_id = Genre.id

select Track.title, Artist.name, Album.title, Genre.name 
    from Track join Genre join Album join Artist on Track.genre_id = Genre.id 
        and Track.album_id = Album.id 
        and Album.artist_id = Artist.id


// track.py 

SELECT Track.title, Album.title, Artist.name FROM Track JOIN Album JOIN Artist
	ON Track.album_id = Album.id AND Album.artist_id = Artist.id

// Assignment
SELECT Track.title, Artist.name, Album.title, Genre.name 
    FROM Track JOIN Genre JOIN Album JOIN Artist 
    ON Track.genre_id = Genre.ID and Track.album_id = Album.id 
        AND Album.artist_id = Artist.id
    ORDER BY Artist.name LIMIT 3



