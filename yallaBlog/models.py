from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models
from datetime  import datetime
# Create your models here.


# class login (models.Model):
# 	username= models.CharField(max_length = 200)
# 	password= models.CharField(max_length = 200)
# 	blockornot= models.CharField(max_length = 200)
	
	
class category_table (models.Model):
	name= models.CharField(max_length = 200)

class posts (models.Model):
	title= models.CharField(max_length = 200)
	post=models.CharField(max_length = 200)
	category=models.CharField(max_length = 200)
	comment=models.CharField(max_length = 200)
	#postdate=models.DateTimeField()
	userpost = models.ForeignKey(User)
	#categ = models.ForeignKey(category)
	cat = models.ForeignKey(category_table)
	image = models.ImageField(upload_to = 'images/', default = 'images/None/no-img.jpg')
	#categorycolumn = models.ForeignKey(category)





