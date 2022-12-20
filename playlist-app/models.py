"""Models for Playlist app."""

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Playlist(db.Model):
    """Playlist."""
    __tablename__="playlists"

    # ADD THE NECESSARY CODE HERE
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text, nullable= False)
    description= db.Column(db.Text, nullable= False)
    songs = db.relationship('Song', secondary= 'playlist_song', backref = 'playlists')


class Song(db.Model):
    """Song."""
    __tablename__="songs"

    # ADD THE NECESSARY CODE HERE
    id = db.Column(db.Integer, primary_key=True)
    title= db.Column(db.Text, nullable= False)
    artist= db.Column(db.Text, nullable= False)
    playlist_song= db.relationship('PlaylistSong', backref = 'songs')


class PlaylistSong(db.Model):
    """Mapping of a playlist to a song."""

    # ADD THE NECESSARY CODE HERE
    __tablename__="playlist_song"
    
    id = db.Column(db.Integer, primary_key=True)
    playlist_id = db.Column(db.Integer, db.ForeignKey(
        'playlists.id'), primary_key=True)
    song_id = db.Column(db.Integer, db.ForeignKey(
        'songs.id'), primary_key=True)
    


# DO NOT MODIFY THIS FUNCTION
def connect_db(app):
    """Connect to database."""

    db.app = app
    db.init_app(app)
