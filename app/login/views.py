# Create your views here.
from django.shortcuts import render, HttpResponse, redirect
  # the index function is called when root is visited
def index(request):
	context = {
     "email" : "blog@gmail.com",
     "name" : "mike"
     }
   	return render(request, "login/index.html", context)

def my_butter(request):
	response = "your personal page sir/mam"
	return HttpResponse(response)