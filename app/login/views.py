# Create your views here.
from django.shortcuts import render, HttpResponse, redirect
  # the index function is called when root is visited
def index(request):
   response = "Hello, I am your first request!"
   return HttpResponse(response)

def my_butter(request):
	response = "your personal page sir/mam"
	return HttpResponse(response)