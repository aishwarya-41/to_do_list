from . import db
from flask_login import UserMixin

class Item(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    data = db.Column(db.String(150))
    user_id = db.Column(db.Integer, db.ForeignKey('user_name.id'))

class User_Name(db.Model,UserMixin):
    __tablename__ = 'user_name'
    id = db.Column(db.Integer,primary_key=True)
    email = db.Column(db.String(150),unique=True)
    name = db.Column(db.String(150))
    password = db.Column(db.String(150))
    items = db.relationship('Item')