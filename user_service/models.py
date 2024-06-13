from peewee import Model, CharField, DateTimeField, ForeignKeyField
from config.database import db
import datetime

class User(Model):
    name = CharField()
    mobile_no = CharField(unique=True, max_length=12)
    email = CharField(unique=True)
    password = CharField()  
    created_at = DateTimeField(default=datetime.datetime.now)

    class Meta:
        database = db

class Follow(Model):
    follower = ForeignKeyField(User, backref='following')
    followee = ForeignKeyField(User, backref='followers')
    created_at = DateTimeField(default=datetime.datetime.now)

    class Meta:
        database = db
