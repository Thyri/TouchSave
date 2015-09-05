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

def profile(request):
	template = "profile.html"

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
	
	u = XUser(
		email = email,
		username = email,
		first_name = fname,
		last_name = lname,
		password=pwd1,
	)
	u.set_password(pwd1)
	
	try:
		u.save()
	except IntegrityError:
		return redirect("/TouchSave/?error=%s" % "duplicateuser")
		
	return loginAux(email, pwd1, request)
	
#####################################################################
#        THE BELOW FUNCTIONS ARE HELPER FUNCTIONS NOT VIEWS         #
#####################################################################	
	
def loginAux(username, password, request):
    u1 = authenticate(username=username, password=password)

    if not u1 is None:
        if u1.is_active:
            login(request, u1)
            print("Login successful for user " + username)
            return HttpResponseRedirect(reverse('profile'))
        else:
            #user is not active
            #redirect to login page with error message
            print("Login failed for user " + username)
            return redirect("/TouchSave/?error=%s" % "authfail")
    else:
        #user does not exist
        #redirect to login page with error message
        print("Login failed for user " + username)
        return redirect("/TouchSave/?error=%s" % "authfail")

		
	

