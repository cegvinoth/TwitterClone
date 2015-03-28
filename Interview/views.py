from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from Interview.models import users,userposts,notifications,follow
from django.template import Context,loader
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.core.exceptions import ObjectDoesNotExist


def index(request):
	if request.session.get('fname',False):
		  userid=request.session['id']
		  return HttpResponseRedirect('/profile?id='+str(userid))
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
				request.session['fname']=login.firstname
				request.session['id']=str(login.id)
			return HttpResponseRedirect('/profile?id='+str(login.id))
		 except ObjectDoesNotExist:  
			login=users.objects.get(email=uname1,password=password1)
			if login.id:
				request.session['fname']=login.firstname
				request.session['id']=str(login.id)
			return HttpResponseRedirect('/profile?id='+str(login.id))
	
	  elif request.POST.get('register',False):
		 try:
			uname=request.POST['uname']
			fname=request.POST['fname']
			lname=request.POST['lname']
			email=request.POST['email']
			password=request.POST['pword']
			register=users(username=uname,firstname=fname,lastname=lname,email=email,password=password)
			register.save()
			request.session['fname']=register.firstname
			request.session['id']=register.id
			return HttpResponseRedirect('/profile?id='+str(register.id))
		 except Exception as e:
			return HttpResponse(e)
			#return HttpResponseRedirect('/')
	  else:
		  return HttpResponseRedirect('/')
	except Exception as e:
	  return HttpResponse(e)
	  #return HttpResponseRedirect('/')

@csrf_exempt
def profile(request):
	if request.session.get('fname',False):
	   name=request.session['fname']
	   userid=request.session['id']
	   pageid=request.GET['id']
	   page=loader.get_template('home.html')
	   resultset=userposts.objects.filter(user_id=pageid).order_by('-created')
	   context=Context({'firstname':name,'resultset':resultset},)
	   return HttpResponse(page.render(context))
	else:
	   return HttpResponseRedirect('/')

def logout(request):
	request.session.flush()
	return HttpResponseRedirect('/')

@csrf_exempt
def postupdate(request):
	if request.session.get('fname',False):
	   data=request.POST['postdata']
	   userid=request.session['id']	
	   postupdate=userposts(post_data=data,user_id=userid)
	   postupdate.save()
	   return HttpResponseRedirect('/')
	else:
	   return HttpResponseRedirect('/')

