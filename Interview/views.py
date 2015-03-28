from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from Interview.models import users
from django.template import Context,loader
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.core.exceptions import ObjectDoesNotExist


def index(request):
	if request.session.get('uname',False):
	      return HttpResponseRedirect('/home')
	page=loader.get_template("index.html")
	context=Context({},)
	return HttpResponse(page.render(context))

@csrf_exempt
def login(request):
	try:
	  if request.POST.get('login',False):
		 try:
			uname1=request.POST['uname1']
			password1=request.POST['pword1']
			login=users.objects.get(username=uname1,password=password1)
			if login.id:
				request.session['uname']=login.username
				request.session['id']=str(login.id)
			return HttpResponseRedirect('/home')
		 except ObjectDoesNotExist:  
			login=users.objects.get(email=uname1,password=password1)
			if login.id:
				request.session['uname']=login.username
				request.session['id']=str(login.id)
			return HttpResponseRedirect('/home')
	
	  elif request.POST.get('register',False):
		 try:
			uname=request.POST['uname']
			fname=request.POST['fname']
			lname=request.POST['lname']
			email=request.POST['email']
			password=request.POST['pword']
			register=users(username=uname,firstname=fname,lastname=lname,email=email,password=password)
			register.save()
			request.session['uname']=register.username
			request.session['id']=register.id
			return HttpResponseRedirect('/home')
		 except Exception as e:
			return HttpResponseRedirect('/')
	  else:
		  return HttpResponseRedirect('/')
	except Exception as e:
	  return HttpResponseRedirect('/')

def home(request):
	if request.session.get('uname',False):
	   name=request.session['uname']
	   userid=request.session['id']
	   return HttpResponse(name+' '+str(userid))
	else:
	   return HttpResponseRedirect('/')

def logout(request):
	request.session.flush()
	return HttpResponseRedirect('/')
	


