from django.db import models
import mongoengine
# Create your models here.
class ashey():
    name = mongoengine.StringField(max_length=200)
    pub_date = mongoengine.DateTimeField(help_text='date published')
    # choices = ListField(EmbeddedDocumentField(Choice))

meta = {
    'indexes': [
        'question', 
        ('pub_date', '+question')
    ]
}