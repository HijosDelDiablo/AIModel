from datetime import datetime


from mongoengine import Document, StringField, DateField

class Metadata(Document):
    model = StringField(required=True)
    tokens = StringField(required=True)
    last_updated = DateField(required=True, default=datetime.now())