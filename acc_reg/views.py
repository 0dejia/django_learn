# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponseRedirect
from django.shortcuts import render
from .form import RegisterForm, LoginForm
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth import authenticate
# Create your views here.

def register(request):
	if request.method == 'POST':
		form = RegisterForm(request.POST)
		if form.is_valid():
			return createUser(request)
	else:
		form = RegisterForm()

	return render(request, 'acc_reg/register.html', {'form':form})

def createUser(request):
	try:
		user = User.objects.create_user(request.POST['username'], request.POST['email'], request.POST['password'])
		user.save()
	except IntegrityError:
		errorMsg = "Username has created, please register other new username!"
		return render(request, 'acc_reg/thank.html', {'text':request.POST['username'], 'errorMsg': errorMsg})

	return render(request, 'acc_reg/thank.html', {'text':request.POST['username']+" created success!"})

def login(request):
	if request.method == "POST":
		form = LoginForm(request.POST)
		if form.is_valid():
			return loginAuthenticate(request)
	else:
		form = LoginForm()

	return render(request, 'acc_reg/login.html', {'form':form})

def loginAuthenticate(request):
	user = authenticate(username=request.POST['username'], password=request.POST['password'])
	if user is not None:
		if user.is_active:
			msg = "User is valid, active and authenticated"
		else:
			msg = "The password is valid, but the account has been disabled!"
	else:
		msg = "The username and password were incorrect"

	return render(request, 'acc_reg/loginMsg.html', {'msg':msg})