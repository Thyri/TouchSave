from django.shortcuts import render, redirect
from TouchSave_App.models import *
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse
from django.core.mail import send_mail
from django.core.urlresolvers import reverse
from django.db import IntegrityError
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
def index(request):
	template = "index.html"
	context = {}
	return render(request,template, context)
	#return HttpResponse("HELLO WORLD")

def profile(request):
	template = "profile.html"
	return render(request, template, {})
	#return HttpResponse("yo")

@csrf_exempt
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
		date_of_birth = null,
		blood_type = null,
		
	)
	u.set_password(pwd1)
	
	try:
		u.save()
	except IntegrityError:
		return redirect("/TouchSave/?error=%s" % "duplicateuser")
		
	return loginAux(email, pwd1, request)
	

def modProfile(request):
	
	name = request.POST['nname']
	dob = request.POST['dname']
	blood = request.POST['bname']
	allergies = request.POST['aname']
	
#####################################################################
#        THE BELOW FUNCTIONS ARE HELPER FUNCTIONS NOT VIEWS         #
#####################################################################	
	
def loginAux(username, password, request):
    u1 = authenticate(username=username, password=password)

    if not u1 is None:
        if u1.is_active:
            login(request, u1)
            print("Login successful for user " + username)
            return render(request, "profile.html", {})
        else:
            #user is not active
            #redirect to login page with error message
            print("Login failed for user " + username)
            return redirect("/TouchSave/?error=%s/the nested else" % "authfail")
    else:
        #user does not exist
        #redirect to login page with error message
        print("Login failed for user " + username)
        return redirect("/TouchSave/?error=%s" % "authfail")

		
	

