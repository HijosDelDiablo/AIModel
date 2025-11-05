from datetime import datetime
from models import User

from mongoengine import Document, ListField, ReferenceField


class Conversation(Document):
    # relations 
    user = ReferenceField(User)
    