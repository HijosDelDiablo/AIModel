from datetime import datetime
from models import User, Session

from mongoengine import Document, ListField, ReferenceField, DateField


class Conversation(Document):
    # relations 
    user = ReferenceField(User)
    session = ReferenceField(Session)

    # attributes
    created_at = DateField(required=True, default=datetime.now())
    updated_at = DateField(required=True, default=datetime.now())
    