# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponseRedirect
from django.shortcuts import render
from .form import RegisterForm
from django.contrib.auth.models import User
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
	user = User.objects.create_user(request.POST['username'], request.POST['email'], request.POST['password'])
	user.save()
	return render(request, 'acc_reg/thank.html', {'text':request.POST['username']})
