from django.db import models

# Create your models here
class users(models.Model):
	  username=models.CharField(max_length=50,unique=True)
	  firstname=models.CharField(max_length=24)
	  lastname=models.CharField(max_length=24)
	  email=models.EmailField(unique=True)
	  password=models.CharField(max_length=24)

class follow(models.Model):
	  user_id=models.ForeignKey(users)
	  following_id=models.IntegerField()
	  created=models.DateTimeField(auto_now_add=True)

class notifications(models.Model):
	  notify_type=models.CharField(max_length=50)
	  notify_createdby=models.IntegerField()
	  notify_post_id=models.IntegerField()

class userposts(models.Model):
	  post_data=models.CharField(max_length=1000)
	  user_id=models.IntegerField()
	  created=models.DateTimeField(auto_now_add=True)


