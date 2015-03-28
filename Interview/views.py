from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from Interview.models import users,userposts,follow
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
	   userid=int(request.session['id'])
	   pageid=int(request.GET['id'])
	   followcode=""
	   if userid != pageid:
		 try:
		  followdata=follow.objects.get(user_id_id=userid,following_id=pageid)
		  if followdata.id:
			followcode="<input type='submit' name='unfollow' value='unfollow'>"
		 except ObjectDoesNotExist:
			followcode="<input type='submit' name='follow' value='follow'>"
	   page=loader.get_template('home.html')
	   resultset=userposts.objects.filter(user_id=pageid).order_by('-created')
	   context=Context({'firstname':name,'resultset':resultset,'pageid':pageid,'followcode':followcode},)
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
	   postupdate=userposts(post_data=data,user_id_id=userid)
	   postupdate.save()
	   return HttpResponseRedirect('/')
	else:
	   return HttpResponseRedirect('/')

@csrf_exempt
def followuser(request):
	pageid=request.POST['pageid']
	userid=request.session['id']
	if request.POST.get('follow',False):
	   followquery=follow(user_id_id=userid,following_id=pageid)
	   followquery.save()
	elif request.POST.get('unfollow',False):
	   followquery=follow.objects.filter(user_id_id=userid,following_id=pageid)
	   followquery.delete()
	return HttpResponseRedirect('/profile?id='+pageid)

def notifications(request):
	if request.session.get('fname',False):
	   userid=request.session['id']
	   followdata=follow.objects.filter(user_id_id=userid).values('following_id')
	   postdata=userposts.objects.filter(user_id__in=followdata).order_by('-created')
	   page=loader.get_template("notifications.html")
	   context=Context({'postdata':postdata},)
	   return HttpResponse(page.render(context))
	else:
	  return HttpResponseRedirect('/')


