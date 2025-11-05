from datetime import datetime

from mongoengine import Document, StringField, DateTimeField


class Message(Document):

    participant = StringField(required=True)    # user or bot
    content = StringField(required=True)  # message text
    sent_at = DateTimeField(required=True, default=datetime.now()) # timestamp