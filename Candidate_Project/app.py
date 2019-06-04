from flask import Flask, render_template, request, redirect
# from flask_restful import Resource, Api
from flask_triangle import Triangle
#from flask_heroku import Heroku #environment variables
from flask_sqlalchemy import SQLAlchemy
import sys, json # necessary?
import os # os allows for retrieval of environment variables (done in test, but may not be necessary with flask_heroku)

app = Flask(__name__)
Triangle(app) # allows for AngularJS expressions filter
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# TEMP - set database URI for local testing of database entries
#app.config['SQLALCHEMY_DATABASE_URI'] = "postgres:///music_db"
app.config.from_object(os.environ['APP_SETTINGS'])
#heroku = Heroku(app) # environment variables taken care of and database config set up
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

#db.create_all()
# retrieve list of music entries from database
musicList = MusicEntry.query.all() # need to add musicList to render_template later
editItem = {}
editId = 0

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
    editId = request.form.get("idNum")
    editSelection = MusicEntry.query.filter_by(id=editId).first()
    # editSelection.song = newname
    # db.session.commit()
    return render_template('entryUpdate.html', editItem=editSelection)

@app.route("/update2", methods=["POST"])
def update2():
    editId = request.form.get("idNum")
    updatedSongName = request.form.get("updatedSongName")
    updatedArtistName = request.form.get("updatedArtistName")
    updatedAlbumTitle = request.form.get("updatedAlbumTitle")
    updatedYear = request.form.get("updatedYear")
    updatedRating = request.form.get("updatedRating")
    editSelection = MusicEntry.query.filter_by(id=editId).first()
    editSelection.song = updatedSongName
    editSelection.artist = updatedArtistName
    editSelection.album = updatedAlbumTitle
    editSelection.year = updatedYear
    editSelection.rating_0_5 = updatedRating
    db.session.commit()
    return redirect("/")

@app.route("/delete", methods=["POST"])
def delete():
    name = request.form.get("name")
    editSelection = MusicEntry.query.filter_by(song=name).first()
    db.session.delete(editSelection)
    db.session.commit()
    return redirect("/")

if __name__ == '__main__':
    app.run()
