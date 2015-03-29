from django.db import models

# Create your models here
class users(models.Model):
	  username=models.CharField(max_length=50,unique=True,null=False)
	  firstname=models.CharField(max_length=24,null=False)
	  lastname=models.CharField(max_length=24,null=False)
	  email=models.EmailField(unique=True,null=False)
	  password=models.CharField(max_length=24,null=False)

class follow(models.Model):
	  user_id=models.ForeignKey(users)
	  following_id=models.IntegerField()
	  created=models.DateTimeField(auto_now_add=True)

class userposts(models.Model):
	  post_data=models.CharField(max_length=1000,null=False)
	  user_id=models.ForeignKey(users)
	  created=models.DateTimeField(auto_now_add=True)


