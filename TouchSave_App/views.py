from django.shortcuts import render, redirect
from TouchSave_App.models import *
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse
from django.core.mail import send_mail
from django.core.urlresolvers import reverse
from django.db import IntegrityError
from django.views.decorators.csrf import csrf_exempt
from django.conf.urls import url



# Create your views here.
def index(request):
	template = "index.html"
	context = {}
	return render(request,template, context)
	#return HttpResponse("HELLO WORLD")

def profile(request, user_id):
	user = XUser.objects.get(id=user_id)
	
	fname = user.first_name
	lname = user.last_name
	
	allergy_list = Allergies.objects.filter(user_with_allergy=user)
	comment = Comments.objects.filter(users_commen=user)
	
	dob = user.date_of_birth
	blood = user.blood_type
	
	
	if blood == 'k':
		blood = None

	#d=None
		
	context = {
		'user' : user,
		'fname' : fname,
		'lname' : lname,
		'dob' : dob,
		'blood_type' : blood,
		'allergies' : allergy_list,
		'comments' : comment,
	}
	
	template = "profile.html"
	
	return render(request, template, context)
	

@csrf_exempt
def register(request):

	email = request.POST['reg_email']
	fname = request.POST['reg_fname']
	lname = request.POST['reg_lname']
	dob = request.POST['reg_dob']
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
		date_of_birth = dob,
		blood_type = 'k',
	)
	u.set_password(pwd1)
	
	try:
		u.save()
	except IntegrityError:
		return redirect("/TouchSave/?error=%s" % "duplicateuser")
		
	return loginAux(email, pwd1, request)

@csrf_exempt
def log_user(request):
	email = request.POST['login_email']
	pwd = request.POST['login_pwd']
	
	return loginAux(email, pwd, request)

@csrf_exempt	
def edit_profile(request):
	user = XUser.objects.get(pk=request.user.id)
	
	fname = user.first_name
	lname = user.last_name
	
	allergy_list = Allergies.objects.filter(user_with_allergy=user)
	comment = Comments.objects.filter(users_commen=user)
	
	date = user.date_of_birth
	blood_t = user.blood_type
		
	if (blood_t == 'k'):
		blood = None
	else:
		blood = blood_t
		
	context = {
		'user' : user,
		'fname' : fname,
		'lname' : lname,
		'dob' : dob,
		'blood_type' : blood,
		'allergies' : allergy_list,
		'comments' : comment,
	}
	
	template = "edit.html"
	
	return render(request, template, context)

@csrf_exempt	
def update(request):
	user = XUser.objects.get(pk=request.user.id)

	fname = request.POST['fname']
	lname = request.POST['lname']
	dob = request.POST['dob']
	blood_t = request.POST['blood_type']
	
	known_allergies = request.POST['allergies']
	known_allergies = known_allergies.split(',')
	for allergy_str in known_allergies:
		a =  Allergies{
			allergy = allergy_str,
			user_with_allergy = user
		}
		a.save()
	
	comment = request.POST['comment']
	c = Comments{
	    comment = comment,
		users_commen = user
	}
	
	c.save()
	
	user.first_name = fname
	user.last_name = lname
	user.date_of_birth = dob
	user.blood_type = blood_t
	
	user.save()
	
	allergy_list = Allergies.objects.filter(user_with_allergy=user)
	comment = Comments.objects.filter(users_commen=user)
	
	if (blood_t == 'k'):
		blood = None
	else:
		blood = blood_t
	
	template = "profile.html"
	context = {
		'user' : user,
		'fname' : fname,
		'lname' : lname,
		'dob' : dob,
		'blood_type' : blood_t,
		'allergies' : allergy_list,
		'comments' : comment,
	}
	
	return render(request, template, context)
	
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
	
    if not u1 is None or username!=None:
        if u1.is_active:
            login(request, u1)
            print("Login successful for user " + username)
            return HttpResponseRedirect(reverse('profile', kwargs={'user_id':request.user.id}))
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

		
	

