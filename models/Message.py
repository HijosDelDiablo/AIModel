from datetime import datetime

from mongoengine import Document, StringField, DateTimeField, EmbeddedDocument


class Message(EmbeddedDocument):

    participant = StringField(required=True)    # user or bot
    content = StringField(required=True)  # message text
    sent_at = DateTimeField(required=True, default=datetime.now()) # timestamp