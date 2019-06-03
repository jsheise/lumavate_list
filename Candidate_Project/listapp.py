from flask import Flask, render_template, request
# from flask_restful import Resource, Api
from flask_triangle import Triangle

from flask_heroku import Heroku #environment variables
from flask_sqlalchemy import SQLAlchemy

import sys, json # necessary?
import os # os allows for retrieval of environment variables (done in test, but may not be necessary with flask_heroku)

# taken from https://www.codementor.io/garethdwyer/building-a-crud-application-with-flask-and-sqlalchemy-dm3wv7yu2
# (got an error with music_db cannot be found)
project_dir = os.path.dirname(os.path.abspath(__file__))
database_file = "postgresql:///{}".format(os.path.join(project_dir, "music_database.db"))


app = Flask(__name__)
Triangle(app) # allows for AngularJS expressions filter
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# TEMP - set database URI for local testing of database entries
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql:///music_db"
heroku = Heroku(app) # environment variables taken care of and database config set up
db = SQLAlchemy(app) # database object

# CAN be put in separate file, but no need here
class MusicEntry(db.Model):
    id = db.Column(db.Integer, primary_key=True) # establish id for entries
    song = db.Column(db.String()) # string has limit of 255 chars, text has 30,000
    artist = db.Column(db.String())
    album = db.Column(db.String())
    year = db.Column(db.Integer())
    rating_0_5 = db.Column(db.Integer())

    def __init__(self, song, artist, album, year, rating): # FINISH THIS LATER WITH MORE UNDERSTANDING
        self.song = song
        self.artist = artist
        self.album = album
        self.year = year
        self.rating = rating

    # "define how to represent our book object as a string. This allows us to do things like print(book), and see meaningful output."
    def __repr__(self):
        return '<id {}>'.format(self.id)

    def serialize(self):
        return {
            'id': self.id,
            'song': self.song,
            'artist': self.artist,
            'album': self.album,
            'year':self.year,
            'rating':self.rating
        }

# retrieve list of music entries from database
# musicList = MusicEntry.query.all() # need to add musicList to render_template later

@app.route('/', methods=["POST", "GET"])
def home():
    if request.form:
        newEntry = MusicEntry(song=request.form.get("newSongName"), artist=request.form.get("newArtist"), album=request.form.get("newAlbum"), year=request.form.get("newYear"), rating=request.form.get("newRating"))
        db.session.add(newEntry)
        db.session.commit()
    return render_template('list.html') #, entryData = EntryData)

if __name__ == '__main__':
    app.run(debug=True)

# BELOW IS USING flask_restful LIBRARY
# EntryData = EntryData

# api = Api(app)
#
# class ListItem(Resource):
#     def get(self):
#         return render_template('list.html');
#
# api.add_resource(ListItem, '/')
