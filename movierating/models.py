from datetime import datetime
from movierating import db, login_manager
from flask_login import UserMixin


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


movie_genre = db.Table('movie_genre',
                       db.Column('movie_id', db.Integer,
                                 db.ForeignKey('movie.id'), nullable=False),
                       db.Column('genre_id', db.Integer,
                                 db.ForeignKey('genre.id'), nullable=False),
                       db.PrimaryKeyConstraint('movie_id', 'genre_id'))


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(40), unique=True, nullable=False)
    email = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)
    movies = db.relationship('Movie', backref='uploader', lazy=True)
    is_admin = db.Column(db.Boolean(), default=False)


class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50), unique=True, nullable=False)
    slug = db.Column(db.String(80), unique=True, nullable=False)
    genres = db.relationship('Genre', secondary=movie_genre, backref='movies')
    poster = db.Column(db.String(100), nullable=False)
    cover = db.Column(db.String(100))
    trailer = db.Column(db.String(300), nullable=False)
    storyline = db.Column(db.String(120), nullable=False)
    director = db.Column(db.String(50), nullable=False)
    release_date = db.Column(db.DateTime, nullable=False)
    stars = db.Column(db.String(200), nullable=False)
    runtime = db.Column(db.DateTime, nullable=False)
    uploader_id = db.Column(db.Integer, db.ForeignKey('user.id'),
                            nullable=False)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return self.title


class Genre(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), unique=True, nullable=False)

    def __repr__(self):
        return self.name
