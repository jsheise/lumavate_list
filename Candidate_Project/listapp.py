from flask import Flask, render_template, request, redirect
# from flask_restful import Resource, Api
from flask_triangle import Triangle

from flask_heroku import Heroku #environment variables
from flask_sqlalchemy import SQLAlchemy

import sys, json # necessary?
import os # os allows for retrieval of environment variables (done in test, but may not be necessary with flask_heroku)

# taken from https://www.codementor.io/garethdwyer/building-a-crud-application-with-flask-and-sqlalchemy-dm3wv7yu2
# (got an error with music_db cannot be found)
#project_dir = os.path.dirname(os.path.abspath(__file__))
#database_file = "postgresql:///{}".format(os.path.join(project_dir, "music_database.db"))


app = Flask(__name__)
Triangle(app) # allows for AngularJS expressions filter
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# TEMP - set database URI for local testing of database entries
app.config['SQLALCHEMY_DATABASE_URI'] = "postgres:///music_db"
heroku = Heroku(app) # environment variables taken care of and database config set up
db = SQLAlchemy(app) # database object

# CAN be put in separate file, but no need here
class MusicEntry(db.Model):
    __tablename__ = "music_table"
    id = db.Column(db.Integer, primary_key=True) # establish id for entries
    song = db.Column(db.String()) # string has limit of 255 chars, text has 30,000
    artist = db.Column(db.String())
    album = db.Column(db.String())
    year = db.Column(db.Integer())
    rating_0_5 = db.Column(db.Integer())

    def __init__(self, song, artist, album, year, rating_0_5): # FINISH THIS LATER WITH MORE UNDERSTANDING
        self.song = song
        self.artist = artist
        self.album = album
        self.year = year
        self.rating_0_5 = rating_0_5

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
            'rating_0_5':self.rating_0_5
        }

# retrieve list of music entries from database
musicList = MusicEntry.query.all() # need to add musicList to render_template later

@app.route('/', methods=["POST", "GET"])
def home():
    if request.form:
        newEntry = MusicEntry(song=request.form.get("newSongName"), artist=request.form.get("newArtist"), album=request.form.get("newAlbum"), year=request.form.get("newYear"), rating_0_5=request.form.get("newRating"))
        db.session.add(newEntry)
        db.session.commit()
    musicList = MusicEntry.query.all()
    return render_template('list.html', musicList=musicList) #, entryData = EntryData)

@app.route("/update", methods=["POST"])
def update():
    newname = request.form.get("newname")
    oldname = request.form.get("oldname")
    editSelection = MusicEntry.query.filter_by(song=oldname).first()
    editSelection.title = newname
    db.session.commit()
    return redirect("/")

@app.route("/delete", methods=["POST"])
def delete():
    name = request.form.get("name")
    editSelection = MusicEntry.query.filter_by(song=name).first()
    db.session.delete(editSelection)
    db.session.commit()
    return redirect("/")

# @app.route('/addEntry', methods=["POST"])
# def addEntry():
#     try:
#         json_data = request.json['newEntry']
#         songName = json_data[song]
#         artistName = json_data[artist]
#         albumName = json_data[album]
#         yearNum = json_data[year]
#         ratingNum = json_data[rating]
#
#         newMusicEntry = MusicEntry(song=songName, artist=artistName, album=albumName, year=yearNum, rating_0_5=ratingNum)
#         db.session.add(newMusicEntry)
#         db.session.commit()
#         return render_template('list.html', musicList=musicList) #, entryData = EntryData)
#     except Exception(e):
#         return str(e)
#     return 'added'

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
