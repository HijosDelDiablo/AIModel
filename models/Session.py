from datetime import datetime

from mongoengine import Document, StringField, EmailField, IntField, DateField


class Session(Document):
    date_at = DateField(required=True, default=datetime.now())
    date_modified = DateField(required=True, default=datetime.now())
    