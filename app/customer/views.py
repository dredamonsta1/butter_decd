# Create your views here.
# Create your views here.
from django.shortcuts import render, HttpResponse, redirect
  # the index function is called when root is visited
def index(request):
   response = "Heyyyyyyyyyyyyyyyyyyyy!"
   return HttpResponse(response)


def people(request):
 context = {
     "email" : "blog@gmail.com",
     "name" : "mike"
 }
 return render(request, "login/index.html", context)