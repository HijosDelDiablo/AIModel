from datetime import datetime
from .User import User
from .Session import Session
from .Message import Message
from .Metadata import Metadata

from mongoengine import Document, ListField, ReferenceField, DateField


class Conversation(Document):
    # relations id

    session = ReferenceField(Session)

    # relations embedded