from catalog_app import db
from datetime import datetime


class Player(db.Model):
    """ A player is equivalent to a user of the web application

        Attributes:
            email: a player's email when first signed in via Oauth
            username: a player's full name returned by Google Oauth API
            picture: a link to the profile picture returned by Google Oauth API
            password_hash: currently store the user's sub ID returned by Google
            created: timestamp
    """
    __tablename__ = 'players'
    email = db.Column(db.String(50), index=True, primary_key=True)
    username = db.Column(db.String(100))
    picture = db.Column(db.String(200), nullable=False, default='default.jpg')
    password_hash = db.Column(db.String(64), nullable=False)
    created = db.Column(db.DateTime, default=datetime.utcnow)
    created_by = db.relationship('Toon', backref='player', lazy=True)

    @property
    def serialize(self):
        return {
            'email': self.email,
            'username': self.username,
            'picture': self.picture,
            'created': self.created,
        }


class Class(db.Model):
    """ A class is a 'type' of gaming character that a user can play

        Attributes:
            class_name: name of the class of a game character
            class_info: additional info of the class of a game character
    """
    __tablename__ = 'classes'
    id = db.Column(db.Integer, primary_key=True)
    class_name = db.Column(db.String(30), nullable=False)
    class_info = db.Column(db.String(500))
    toons = db.relationship('Toon', backref='toon_class', lazy=True)

    @property
    def serialize(self):
        return {
            'id': self.id,
            'class_name': self.class_name,
            'class_info': self.class_info,
        }


class Toon(db.Model):
    """ A toon is the character that a player is playing with

        Attributes:
            name: name of a game character
            description: description of a game character entered by a player
            created: timestamp
    """
    __tablename__ = 'toons'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), nullable=False)
    description = db.Column(db.String(500), nullable=False)
    created = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    toon_class_id = db.Column(db.Integer, db.ForeignKey('classes.id'),
                              nullable=False)
    toon_player = db.Column(db.String(50), db.ForeignKey('players.email'),
                            nullable=False)

    @property
    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'created': self.created,
            'toon_class': self.toon_class.class_name,
            'toon_player': self.toon_player,
        }
