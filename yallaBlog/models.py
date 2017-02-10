from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models
from datetime  import datetime
from django.utils import timezone
# Create your models here.


# class login (models.Model):
# 	username= models.CharField(max_length = 200)
# 	password= models.CharField(max_length = 200)
# 	blockornot= models.CharField(max_length = 200)
	
	
class category_table (models.Model):
	name= models.CharField(max_length = 200)
	user = models.ManyToManyField(User, blank=True)
	def __str__(self):
		return self.name
    	

class posts (models.Model):
	# post_date=models.DateField(auto_now_add = True)
	title= models.CharField(max_length = 200)
	post=models.CharField(max_length = 200)
	#category=models.CharField(max_length = 200)
	comment=models.CharField(max_length = 200)
	#postdate=models.DateTimeField()
	userpost = models.ForeignKey(User)
	#categ = models.ForeignKey(category)
	cat = models.ForeignKey(category_table)
	
	image = models.ImageField(upload_to = './images/', default='images/None/no-img.jpg')
	#categorycolumn = models.ForeignKey(category)
	# image = models.ImageField(upload_to = 'static/images/' , blank=True)
	

	def __str__(self):
		return self.title
        

# , default = 'images/None/no-img.jpg'
# class subscribe (models.Model):
# 	category = models.ForeignKey(category_table)
# 	name = models.ForeignKey(User)
# 	subscribe = models.CharField(default = 'subscribe', max_length = 200)
# 	def __str__(self):
# 		return self.subscribe
        


# class badword (models.Model):
# 	word= models.CharField(max_length = 200)
# 	def __str__(self):
# 		return self.word



# class Comment(models.Model):
#     post = models.ForeignKey(posts , related_name='comments')
#     author = models.ForeignKey(User)
#     text = models.TextField()
#     created_date = models.DateTimeField(default=timezone.now)
#     approved_comment = models.BooleanField(default=True)

#     # def approve(self):
#     #     self.approved_comment = True
#     #     self.save()

#     def __str__(self):
#         return self.text

class badword (models.Model):
	rude_word= models.CharField(max_length = 200)
	def __str__(self):
		return self.rude_word



class Comment(models.Model):
    post = models.ForeignKey(posts , related_name='comments')
    author = models.ForeignKey(User)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    approved_comment = models.BooleanField(default=True)


    def check_func(self):
		bad_words=badword.objects.all()
		temp=""
		commentcheck=self.text.split()
		for word in commentcheck:
			for bad in bad_words:
				if word == bad.rude_word:
					word=len(word)*"*"
					break
			temp+=" "
			temp+=word
		self.text=temp
		self.save()


    def __str__(self):
        return self.text

class Reply(models.Model):
    post = models.ForeignKey(posts , related_name='replys')
    comment = models.ForeignKey(Comment , related_name='replys')
    author = models.ForeignKey(User)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)

    def check_func(self):
		bad_words=badword.objects.all()
		temp=""
		commentcheck=self.text.split()
		for word in commentcheck:
			for bad in bad_words:
				if word == bad.rude_word:
					word=len(word)*"*"
					break
			temp+=" "
			temp+=word
		self.text=temp
		self.save()
    
    def __str__(self):
        return self.text


