from peewee import Model, ForeignKeyField, DateTimeField, TextField, IntegerField
from config.database import db
import datetime
from user_service.models import User
from discussion_service.models import Discussion

class Comment(Model):
    user = ForeignKeyField(User, backref='comments')
    discussion = ForeignKeyField(Discussion, backref='comments')
    text = TextField()
    parent_comment = ForeignKeyField('self', null=True, backref='replies')
    created_at = DateTimeField(default=datetime.datetime.now)

    class Meta:
        database = db

class Like(Model):
    user = ForeignKeyField(User, backref='likes')
    comment = ForeignKeyField(Comment, backref='likes', null=True)
    discussion = ForeignKeyField(Discussion, backref='likes', null=True)
    created_at = DateTimeField(default=datetime.datetime.now)

    class Meta:
        database = db

class View(Model):
    user = ForeignKeyField(User, backref='views')
    discussion = ForeignKeyField(Discussion, backref='views')
    count = IntegerField(default=0)

    class Meta:
        database = db
