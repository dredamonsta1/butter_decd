from django.conf.urls import url
from . import views           # This line is new!
urlpatterns = [
	url(r'^trip$', views.people)     # This line has changed!
  ]