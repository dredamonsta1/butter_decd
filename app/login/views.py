# Create your views here.
from django.shortcuts import render, HttpResponse, redirect
# from .forms import NameForm
import mongoengine
# from mongoengine.django.auth import User
# user = authenticate(username=username, password=password)
# assert isinstance(user, mongoengine.django.auth.User)

  # the index function is called when root is visited
def index(request):
	context = {
     "email" : "blog@gmail.com",
     "name" : "first_name Andre"
     }
   	return render(request, "login/index.html", context)

def my_butter(request):
	response = "this view is from def mybutter in login view"
	return HttpResponse(response)


def log_reg(request):
	if request.method == "POST":
		form = NameForm(request.POST)
		# if form.is_valid():
			

		# print "*"*20
		# print request.POST
		# print request.method
		# print "*"*20
		# return render(request, "login/sign_in.html")
	# else:
		# form = NameForm()
	return render(request, "login/sign_in.html", {'form':form})