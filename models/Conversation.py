from datetime import datetime
from .User import User
from .Session import Session
from .Message import Message
from .Metadata import Metadata

from mongoengine import Document, ListField, ReferenceField, DateField


class Conversation(Document):
    # relations id
    user = ReferenceField(User)
    session = ReferenceField(Session)

    # relations embedded
    messages = ListField(ReferenceField(Message))
    metadata = ReferenceField(Metadata) 


    # attributes
    created_at = DateField(required=True, default=datetime.now())
    updated_at = DateField(required=True, default=datetime.now())
