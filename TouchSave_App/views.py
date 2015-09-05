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
	if request.user.is_authenticated():
		return redirect("/TouchSave/")
	else:
		template = "templates/index.html"
		context = {}
		return render(request,template, context)
	
def register(request):
	email = request.POST['reg_email']
	fname = request.POST['reg_fname']
	lname = request.POST['reg_lname']
	pwd1 = request.POST['reg_pwd1']
	pwd2 = request.POST['reg_pwd2']
	
	if pwd1 != pwd2:
		return redirect("/TouchSave/?error=%s" % "pwdmismatch")
	
	u = XUser{
		email = email,
		username = email,
		
	}
	template = "index.html"
	context = {}
	return render(request,template, context)