# Create your views here.
from django.shortcuts import render, HttpResponse, redirect
import mongoengine
# from mongoengine.django.auth import User
# user = authenticate(username=username, password=password)
# assert isinstance(user, mongoengine.django.auth.User)

  # the index function is called when root is visited
def index(request):
	context = {
     "email" : "blog@gmail.com",
     "name" : "mike"
     }
   	return render(request, "login/index.html", context)

def my_butter(request):
	response = "this view is from def mybutter in login view"
	return HttpResponse(response)


def log_reg(request):
	if request.method == "POST":
		print "*"*20
		print request.POST
		print request.method
		print "*"*20
	return render(request, "login/sign_In.html")