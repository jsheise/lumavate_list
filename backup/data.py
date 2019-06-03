class EntryData:
    def __init___(self, artist, song, album, year, fav):
        self.artist = artist
        self.song = song
        self.album = album
        self.year = year
        self.fav = fav
        self.edit = false

    def change_artist(self, new_artist):
        self.artist = new_artist

    def change_song(self, new_song):
        self.song = new_song

    def change_album(self, new_album):
        self.album = new_album

    def change_year(self, new_year):
        self.year = new_year

    def change_fav(self, new_fav):
        self.fav = new_fav

class EntryList:
    def __init__(self):
        self.entryList = []

    def addEntry(newEntry):
        # Check that the input box has a value
        if(not (newEntry == undefined or newEntry == ""))
          self.entryList.push({newEntry.artist, newEntry.song, newEntry.album, newEntry.year, newEntry.fav})
        

    def deleteEntry = function:
