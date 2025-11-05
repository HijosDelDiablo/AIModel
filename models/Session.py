from datetime import datetime

from mongoengine import Document, StringField, EmailField, IntField, DateField, ReferenceField, ListField, EmbeddedDocumentField

from .Message import  Message
from .Metadata import Metadata
from .User import User

class Session(Document):
    # RELATIONS
    user = ReferenceField(User)
    messages = ListField(EmbeddedDocumentField(Message), required=False, default=[])
    metadata = ReferenceField(Metadata, required=False, default=None)


    # attributes
    created_at = DateField(required=True, default=datetime.now())
    updated_at = DateField(required=True, default=datetime.now())

    
    def to_dict(self):
        """Convierte el documento a diccionario con ObjectId serializado y datos completos del usuario"""
        data = self.to_mongo().to_dict()
        data['_id'] = str(data['_id'])
        if self.user:
            data['user'] = self.user.to_dict() if hasattr(self.user, 'to_dict') else self.user.to_mongo().to_dict()
            data['user']['_id'] = str(data['user']['_id'])
        else:
            data['user'] = None
        return data