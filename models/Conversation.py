from datetime import datetime
from models import User, Session, Message, Metadata

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
