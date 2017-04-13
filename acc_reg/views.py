# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponseRedirect
from django.shortcuts import render
from .form import RegisterForm
# Create your views here.

def register(request):
	if request.method == 'POST':
		form = RegisterForm(request.POST)
		if form.is_valid():
			return HttpResponseRedirect('/thanks/')
	else:
		form = RegisterForm()

	return render(request, 'acc_reg/register.html', {'form':form})