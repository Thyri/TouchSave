from django.shortcuts import render, redirect
from TouchSave_App.models import *
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse
from django.core.mail import send_mail
from django.core.urlresolvers import reverse
from django.db import IntegrityError

# Create your views here.
def index(request):
	template = "index.html"
	context = {}
	return render(request,template, context)
	#return HttpResponse("HELLO WORLD")
