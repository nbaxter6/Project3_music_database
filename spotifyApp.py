# Import all of the necessary dependencies to generate Flask server
import numpy as np

from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine

from flask import Flask, render_template

#################################################
# Database Setup
#################################################
# Connect engine to our sqlite database
engine = create_engine("sqlite:///spotifyApp.sqlite")

# Reflect our entire database into sqlalchemy automap_base function
# This variable allows us to map our entire database schema without exlicitly typing it out in this application
Base = automap_base()
# Automap all of the tables of each database
Base.prepare(autoload_with=engine)

# Save references to each table in database
tract_info = Base.classes.tract_info
track_properties = Base.classes.track_properties
listener_experience = Base.classes.listener_experience
charts = Base.classes.charts
playlists = Base.classes.playlists

#################################################
# Flask Setup
#################################################
app = Flask(__name__)

#################################################
# Flask Routes
#################################################

# Create welcome page on our local server to list all of the pages on our server
@app.route("/")
def welcome():
    """List all available api routes."""
    return render_template('index.html')
    
# Create route for our track_names page
@app.route("/api/v1.0/track_names")
def names():
    # Create our session (link) from Python to the DB
    session = Session(engine)

    """Return a list of all song names in entire database"""
    # Query all track names from main music dataset(NOTE: With a bit of code wrangling it is easy to alter this code to query any column from any table in DB)
    results = session.query(tract_info.track_name).all()

    session.close()

    # Convert list of tuples into normal list
    all_names = list(np.ravel(results))

    # Use render_template package of flask to send data to 'names.html' page
    return render_template('names.html', all_names=all_names)

# Create route to house data for 'tract_info' table in DB
@app.route("/api/v1.0/tract_info")
def Info():
    # Create our session (link) from Python to the DB
    session = Session(engine)

    """Return a list of tract_info table data"""
    # Query tract_info table for each column
    results = session.query(tract_info.track_name, tract_info.artists_name, 
                            tract_info.artist_count, tract_info.released_year, 
                            tract_info.released_month, tract_info.released_day).all()

    session.close()

    # Create empty list for data from dictionaries created by for loop below
    all_info = []
    # Create for loop to get data from every row for each column and put it into empty dictionary "info_dict"
    for track_name, artists_name, artist_count, released_year, released_month, released_day in results:
        info_dict = {}
        info_dict["track_name"] = track_name
        info_dict["artists_name"] = artists_name
        info_dict["artist_count"] = artist_count
        info_dict["released_year"] = released_year
        info_dict["released_month"] = released_month
        info_dict["released_day"] = released_day
        all_info.append(info_dict)

    # Use render_template package of flask to send data to 'track_info.html' page
    return render_template('track_info.html', all_info=all_info)

# Create route to house data for 'track_properties' table in DB
@app.route("/api/v1.0/track_properties")
def Properties():
    # Create our session (link) from Python to the DB
    session = Session(engine)

    """Return a list of track_properties table data"""
    # Query entire 'track_properties' table for each column
    results = session.query(track_properties.track_name, track_properties.artists_name, 
                            track_properties.bpm, track_properties.key, 
                            track_properties.mode).all()

    session.close()

    # Create empty list for data from dictionaries created by for loop below
    all_properties = []
    # Create for loop to get data from every row for each column and put it into empty dictionary "properties_dict"
    for track_name, artists_name, bpm, key, mode in results:
        properties_dict = {}
        properties_dict["track_name"] = track_name
        properties_dict["artists_name"] = artists_name
        properties_dict["bpm"] = bpm
        properties_dict["key"] = key
        properties_dict["mode"] = mode
        all_properties.append(properties_dict)

    # Use render_template package of flask to send data to 'track_properties.html' page
    return render_template('track_properties.html', all_properties=all_properties)

# Create route to house data for 'listener_experience' table in DB
@app.route("/api/v1.0/listener_experience")
def Listener():
    # Create our session (link) from Python to the DB
    session = Session(engine)

    """Return a list of listener_experience table data"""
    # Query entire 'listener_experience' table for each column
    results = session.query(listener_experience.track_name, listener_experience.artists_name, 
                            listener_experience.danceablity, listener_experience.valence, 
                            listener_experience.energy, listener_experience.acousticness,
                            listener_experience.instrumentalness, listener_experience.liveness,
                            listener_experience.speechiness).all()

    session.close()

    # Create empty list for data from dictionaries created by for loop below
    all_listener = []
    # Create for loop to get data from every row for each column and put it into empty dictionary "listener_dict"
    for track_name, artists_name, danceablity, valence, energy, acousticness, instrumentalness, liveness, speechiness in results:
        listener_dict = {}
        listener_dict["track_name"] = track_name
        listener_dict["artists_name"] = artists_name
        listener_dict["danceablity"] = danceablity
        listener_dict["valence"] = valence
        listener_dict["energy"] = energy
        listener_dict["acousticness"] = acousticness
        listener_dict["instrumentalness"] = instrumentalness
        listener_dict["liveness"] = liveness
        listener_dict["speechiness"] = speechiness
        all_listener.append(listener_dict)

    # Use render_template package of flask to send data to 'listener_experience.html' page
    return render_template('listener_experience.html', all_listener=all_listener)

# Create route to house data for 'charts' table in DB
@app.route("/api/v1.0/charts")
def Charts():
    # Create our session (link) from Python to the DB
    session = Session(engine)

    """Return a list of all charts table data"""
    # Query entire 'charts' table for each column
    results = session.query(charts.track_name, charts.artists_name, 
                            charts.in_spotify_charts, charts.in_apple_charts, 
                            charts.in_deezer_charts, charts.in_shazam_chart).all()

    session.close()

    # Create empty list for data from dictionaries created by for loop below
    all_charts = []
    # Create for loop to get data from every row for each column and put it into empty dictionary "charts_dict"
    for track_name, artists_name, in_spotify_charts, in_apple_charts, in_deezer_charts, in_shazam_chart in results:
        charts_dict = {}
        charts_dict["track_name"] = track_name
        charts_dict["artists_name"] = artists_name
        charts_dict["in_spotify_charts"] = in_spotify_charts
        charts_dict["in_apple_charts"] = in_apple_charts
        charts_dict["in_deezer_charts"] = in_deezer_charts
        charts_dict["in_shazam_charts"] = in_shazam_chart
        all_charts.append(charts_dict)

    # Use render_template package of flask to send data to 'charts.html' page
    return render_template('charts.html', all_charts=all_charts)

# Create route to house data for 'playlists' table in DB
@app.route("/api/v1.0/playlists")
def Playlists():
    # Create our session (link) from Python to the DB
    session = Session(engine)

    """Return a list of all charts table data"""
    # Query entire playlists table
    results = session.query(playlists.track_name, playlists.artists_name, 
                            playlists.in_spotify_playlists, playlists.in_apple_playlists, 
                            playlists.in_deezer_playlists).all()

    session.close()

    # Create empty list for data from dictionary created by for loop below
    all_playlists = []
    for track_name, artists_name, in_spotify_playlists, in_apple_playlists, in_deezer_playlists in results:
        playlists_dict = {}
        playlists_dict["track_name"] = track_name
        playlists_dict["artists_name"] = artists_name
        playlists_dict["in_spotify_playlists"] = in_spotify_playlists
        playlists_dict["in_apple_playlists"] = in_apple_playlists
        playlists_dict["in_deezer_playlists"] = in_deezer_playlists
        all_playlists.append(playlists_dict)

    # Use render_template package of flask to send data to 'playlists.html' page
    return render_template('playlists.html', all_playlists=all_playlists)

# start up main page of locally served webpage
if __name__ == '__main__':
    app.run(debug=True)
