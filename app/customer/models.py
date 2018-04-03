from django.db import models
from django import forms
# from pymongo import Connection
from bson import ObjectId
from itertools import imap

# Create your models here.

class Model(dict):
	"""
    A simple model that wraps mongodb document
    """
    # __getattr__ = dict.get
    # __delattr__ = dict.__delitem__
    # __setattr__ = dict.__setitem__

class NameForm(forms.Form):
    your_name = forms.CharField(label='Your name', max_length=100)