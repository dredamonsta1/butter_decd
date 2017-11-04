from django.conf.urls import url
from . import views           # This line is new!
urlpatterns = [
	url(r'^people$', views.intro)     # This line has changed!

	# url(r'^people$', views.intro)
  ]