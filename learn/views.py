# Create your views here.
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render_to_response
import datetime
from learn.models import *
from django.contrib import auth
from django.contrib.auth.models import User

def baselearn(request):
	return render_to_response('baselearn.html')

def login(request):
	return render_to_response('login.html')

def study(request):
	return render_to_response('study.html')

def signup(request):
	return render_to_response('signup.html')

def learning(request):
	return render_to_response('learning.html')

def createUser(request):
		if request.method == 'POST':
			username = request.POST['username']
			password = request.POST['password']
			firstname = request.POST['firstname']
			lastname = request.POST['lastname']
			email = request.POST['email']
			address = request.POST['address']
			country = request.POST['country']
			city = request.POST['city']
			dob = request.POST['dob']
			if User.objects.filter(username__exact=username):
				return HttpResponseRedirect('/learn/')
			User.objects.create_user(username=username, password=password, email=email)
			UserProfile.objects.create(username=username, password=password, email=email, firstname=firstname,
									lastname=lastname, dob=dob, address=address, city=city, country=country)
			user = auth.authenticate(username=username, password=password)
			if user is not None:
				usr = QansUserregistration.objects.get(username=username)
				if user.is_active:
					auth.login(request, user)
					return HttpResponseRedirect('/learn/')

def login(request):
		user = request.user
		if user is not None:
			if user.is_active:	
				usr = UserProfile.objects.get(username=user.username)
				return render_to_response('baselearn.html', locals())
		return render_to_response('baselearn.html')

