from datetime import datetime

from mongoengine import Document, StringField, EmailField, IntField, DateField

class User(Document):
    username = StringField(required=True)
    email = EmailField(required=True)
    age = IntField(required=True)
    date_at = DateField(required=True, default=datetime.now())