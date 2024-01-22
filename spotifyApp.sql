sqlite3 spotifyApp.sqlite

CREATE TABLE tract_info(
    track_name VARCHAR NOT NULL,
    artists_name VARCHAR NOT NULL,
    artist_count INT,
    released_year INT,
    released_month INT,
    released_day INT,
    PRIMARY KEY (track_name, artists_name)
);

.mode csv
.import tract_info.csv tract_info

CREATE TABLE track_properties(
    track_name VARCHAR NOT NULL,
    artists_name VARCHAR NOT NULL,
    bpm INT,
    key VARCHAR,
    mode VARCHAR,
    PRIMARY KEY (track_name, artists_name)
);

.mode csv
.import track_properties.csv track_properties

CREATE TABLE listener_experience(
    track_name VARCHAR NOT NULL,
    artists_name VARCHAR NOT NULL,
    danceablity INT,
    valence INT,
    energy INT,
    acousticness INT,
    instrumentalness INT,
	liveness INT,
	speechiness INT,
    PRIMARY KEY (track_name, artists_name)
);

.mode csv
.import listener_experience.csv listener_experience

CREATE TABLE charts(
    track_name VARCHAR NOT NULL,
    artists_name VARCHAR NOT NULL,
    in_spotify_charts INT,
    in_apple_charts INT,
    in_deezer_charts INT,
    in_shazam_chart INT,
    PRIMARY KEY (track_name, artists_name)
    );

.mode csv
.import charts.csv charts

CREATE TABLE playlists(
   track_name VARCHAR NOT NULL,
   artists_name VARCHAR NOT NULL,
   in_spotify_playlists INT,
   in_apple_playlists INT,
   in_deezer_playlists VARCHAR,
   PRIMARY KEY (track_name, artists_name)
);

.mode csv
.import playlists.csv playlists

CREATE TABLE music_dataset_main (
	track_name VARCHAR NOT NULL,
	artists_name VARCHAR NOT NULL,
	artist_count INT,
	released_year INT,
	released_month INT,
	released_day INT,
	in_spotify_playlists INT,
	in_spotify_charts INT,
	streams VARCHAR,
	in_apple_playlists INT,
	in_apple_charts INT,
	in_deezer_playlists VARCHAR,
	in_deezer_charts INT,
	in_shazam_chart INT,
	bpm INT,
	key VARCHAR,
	mode VARCHAR,
	danceablity INT,
	valence INT,
	energy INT,
	acousticness INT,
	instrumentalness INT,
	liveness INT,
	speechiness INT,
    PRIMARY KEY (track_name, artists_name)
);

.mode csv
.import music_dataset_main.csv music_dataset_main