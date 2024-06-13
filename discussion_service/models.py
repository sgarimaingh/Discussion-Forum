from peewee import Model, ForeignKeyField, CharField, TextField, DateTimeField
from config.database import db
import datetime
from user_service.models import User

class Discussion(Model):
    user = ForeignKeyField(User, backref='discussions')
    text = TextField()
    image = CharField(null=True)  #image url
    hashtags = CharField(null=True) #COMMA-SEPARATED HASHTAGS
    created_at = DateTimeField(default=datetime.datetime.now)

    class Meta:
        database = db
