from django.contrib.auth.models import User,Group
from django.conf import settings
from django.contrib import messages
from django.core.mail import send_mail
from django.shortcuts import render, redirect ,get_object_or_404
from django.contrib import auth 
from django.http import HttpResponse,HttpResponseRedirect
from .models import posts,category_table,badword,Comment,Reply
from forms import post_form, UserForm, category_form , badword_form,CommentForm , ReplyForm
from django.core.context_processors import csrf
from django.contrib.auth.views import login
from models import User 

from django.contrib.auth import (authenticate,logout)
from django.core.urlresolvers import reverse_lazy
from django.views import generic
from . import forms
from django.views.generic import TemplateView

from django.http import Http404
# Create your views here.
# def is_excist (request,form_get):
# 	f = form.cleaned_data['username']
# 	user=User.objects.get(username=f)
# 	if(user):
# 		print "already excists"
# 	else:

# def send_email(request):
# 	#send_mail=('subject','message','from_email','to_list',fail_silently=False)
# 	subject='subscribe category using django'
# 	message='Hello -username- you have subscribed successfully in -category name- welcome aboard'
# 	from_email= settings.EMAIL_HOST_USER
# 	to_list= [settings.EMAIL_HOST_USER]
# 	try:
# 		send_mail(subject,message,from_email,to_list, fail_silently=True)
# 		return HttpResponse('true')
# 	except Exception:
# 		message = 'Error'
# 		return HttpResponse('false') 
# 	else:
# 		return HttpResponse('true')
# 		message = 'Send!'


# def show_post(request,id):
# 	post=posts.objects.filter(id=id)
	
# 	context={'postshow':post}
# 	return render(request, 'yallaBlog/showpost.html' ,context)
def homePosts (request):
	current_user = request.user
	all_cat = category_table.objects.all()
	toppost = posts.objects.all()
	toppost1 = reversed(toppost)
	subscribed_cats = category_table.objects.filter(user = current_user.id)
	context = { "subscribedCats": subscribed_cats ,'all_category': all_cat , 'top_posts': toppost1}
	return render(request , 'yallaBlog/category.html' , context)
    

def subscribe(request, cat_id):
	current_user = request.user
	current_user_name=current_user.username
	current_user_email=current_user.email
	current_category=category_table.objects.get(id=cat_id)
	current_category_name=current_category.name
	subject='subscribe category using django'
	message='Hello '+current_user_name+' you have subscribed successfully in   '+current_category_name+'   category ,welcome aboard'
	from_email= settings.EMAIL_HOST_USER
	to_list= [settings.EMAIL_HOST_USER , current_user_email]
	try:
		send_mail(subject,message,from_email,to_list, fail_silently=True)
	except Exception:
		message = 'Error'
	else:
		message = 'Send!'
	subscribed_cats = category_table.objects.get(id = cat_id)
	subscribed_cats.user.add(current_user)
	return HttpResponseRedirect('/yallaBlog/home')
def unsubscribe(request, cat_id):
    current_user = request.user
    subscribed_cats = category_table.objects.get(id = cat_id)
    subscribed_cats.user.remove(current_user)
    return HttpResponseRedirect('/yallaBlog/home')


#subscribe from category page
def homePostsCAT (request, cat_id):
	current_user = request.user
	cur_cat= cat_id
	all_cat = category_table.objects.all()
	cat_post = posts.objects.filter(cat = cat_id)
	subscribed_cats = category_table.objects.filter(user = current_user.id)
	context = { "subscribedCats": subscribed_cats ,'all_category': all_cat , 'cat_posts': cat_post , 'cur_cat':cur_cat}
	return render(request , 'yallaBlog/post.html' , context)


def subscribeCAT(request, cat_id):
	current_user = request.user
	current_user_name=current_user.username
	current_user_email=current_user.email
	current_category=category_table.objects.get(id=cat_id)
	current_category_name=current_category.name
	subject='subscribe category using django'
	message='Hello '+current_user_name+' you have subscribed successfully in   '+current_category_name+'   category ,welcome aboard'
	from_email= settings.EMAIL_HOST_USER
	to_list= [settings.EMAIL_HOST_USER , current_user_email]
	try:
		send_mail(subject,message,from_email,to_list, fail_silently=True)
	except Exception:
		message = 'Error'
	else:
		message = 'Send!'
	subscribed_cats = category_table.objects.get(id = cat_id)
	subscribed_cats.user.add(current_user)
	return HttpResponseRedirect('/yallaBlog/cat/'+cat_id+'/post')
def unsubscribeCAT(request, cat_id):
    current_user = request.user
    subscribed_cats = category_table.objects.get(id = cat_id)
    subscribed_cats.user.remove(current_user)
    return HttpResponseRedirect('/yallaBlog/cat/'+cat_id+'/post')


# def cat_posts(request , id):
# 	current_user = request.user
# 	cat_post = posts.objects.filter(cat = id)
# 	all_cat = category_table.objects.all()
# 	subscribed_cats = category_table.objects.filter(user = current_user.id)
# 	context = {'cat_posts': cat_post,'all_category': all_cat ,"subscribedCats": subscribed_cats  }
# 	#context = {'cat_posts': cat_post,'all_category': all_cat  }
# 	return render(request, 'yallaBlog/post.html' ,context )


def logout_view(request):
     return HttpResponseRedirect(request, 'yallaBlog/category.html',context)

class register(generic.CreateView):
	form_class = forms.UserCreateForm
	success_url = reverse_lazy("login")
	template_name = "yallaBlog/register_form.html"

# def top_post(request):
# 	toppost = posts.objects.all()
# 	# sub_cat = subscribe.objects.all()
# 	all_cat = category_table.objects.all()
# 	context = {'top_posts': toppost,'all_category': all_cat}
# 	return render(request, 'yallaBlog/category.html' ,context)




def All_category(request):
	all_cat = category_table.objects.all()
	context = {'all_category': all_cat}
	return render(request, 'yallaBlog/category.html' ,context)	


def All_posts(request):
	all_post = posts.objects.all()
	context = {'all_posts': all_post}
	return render(request, 'yallaBlog/index.html' ,context)



def details_post(request,id):
	dp=posts.objects.get(id=id)
	context={'detalis_post':dp}
	return render(request, 'yallaBlog/details.html' ,context)


def new_post(request):
	current_user=request.user.id
	form=post_form()
	if request.method=='POST':
		form=post_form(request.POST, request.FILES)
		if form.is_valid():
			post = form.save(commit=False)
			post.userpost_id=current_user
			post.save()
			return HttpResponseRedirect('/yallaBlog/adminlink/adminhome/post/')
	context={'po_form':form}
	return render(request,'yallaBlog/post_form.html',context)	


def edit_post(request, id):
	
	po = posts.objects.get(id= id)
	form = post_form(instance = po)
	if request.method == 'POST':
		form = post_form(request.POST, instance=po)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect('/yallaBlog/adminlink/adminhome/post/')



	context = {'po_form': form}
	return render(request, 'yallaBlog/post_form.html',context)





def del_post(request, id):
	dele= posts.objects.get(id=id)
	dele.delete()
	return HttpResponseRedirect('/yallaBlog/adminlink/adminhome/post/')




def registerForm(request):
	form=UserForm()
	if request.method=='POST':
		form=UserForm(request.POST)
		#form=registerationForm(request.POST)
		if form.is_valid():
			#flagg=user_exsict(form)
			flagg2=email_exsict(form)
			if(flagg2):
				form.save()
				return HttpResponseRedirect('/yallaBlog/login')
			else:
				return HttpResponse('mawgooodd')
	context={'register_form':form}
	return render(request,'yallaBlog/register_form.html',context)
	
	




def email_exsict (form):
			f = form.cleaned_data['email']
			flag=1
			try:
				of=User.objects.get(email=f)
			except User.DoesNotExist :
				flag=1
			else:
				flag=0
			return flag


def custom_login(request):
	flag=request.user.is_active
	if(flag):
		return login(request)       

	else: 
		#return render(request,'yallaBlog/blocked.html')
		messages.warning(request,'sryyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy')
		return login(request)





#just print hello
def adminhome(request):
	all_post = posts.objects.all()
	us = User.objects.all()
	cat = category_table.objects.all()
	bad = badword.objects.all()
	context = {'us_id':us,'cat_id':cat,'bad_id':bad,'all_posts': all_post}
	return render(request, 'adminUser/userdata.html',context )


def details_user(request, us_id):
	try:
		us = User.objects.get(id=us_id)
	except User.DoesNotExist :
		raise Http404("User not found")
	else:
		context = {'user_details': us }
		return render(request, 'adminUser/userdetails.html',context )

class registerFromAdmin(generic.CreateView):
	form_class = forms.UserCreateForm
	success_url = reverse_lazy("adminHome")
	template_name = "yallaBlog/register_form.html"

# delete 
def del_user(request, us_id):
	us = User.objects.get(id=us_id)
	us.delete()
	return HttpResponseRedirect('/yallaBlog/adminlink/adminhome/user/')




class edit_user(generic.UpdateView):
	mdoel=User
	fields=['is_superuser','is_staff','is_active']
	success_url = reverse_lazy("adminHome")
	template_name = "yallaBlog/register_form.html"
	def get_queryset(self, **kwargs):
		user_id = self.kwargs['pk']
		return User.objects.filter(pk=user_id)


#/////////////////////////////////////////////////////////////////
#category

def del_category(request, cat_id):
	cat = category_table.objects.get(id=cat_id)
	cat.delete()
	return HttpResponseRedirect('/yallaBlog/adminlink/adminhome/category/')

def new_category(request):
	form = category_form()
	if request.method == 'POST':
		form = category_form(request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect('/yallaBlog/adminlink/adminhome/category/')

	context = {'cat_form': form}
	return render(request, 'adminUser/category_form.html',context )

def edit_category(request,cat_id):
		cat = category_table.objects.get(id= cat_id)
		form = category_form(instance = cat)
		if request.method == 'POST':
			form = category_form(request.POST, instance=cat)
			if form.is_valid():
				form.save()
				return HttpResponseRedirect('/yallaBlog/adminlink/adminhome/category/')
		context = {'cat_form': form}
		return render(request, 'adminUser/category_form.html',context)
# # edit

# class edit_user(generic.CreateView):
# 	def get(self):
# 		us = User.objects.get(id=self.args['us_id'])
# 		form_class = forms.UserCreateForm(instance = us)
# 		success_url = reverse_lazy("adminHome")
# 		template_name = "/yallaBlog/register_form.html"
# 		return HttpResponseRedirect('/yallaBlog/user/new')

	# us = student.objects.get(id= us_id)
	# form = forms.UserCreateForm(instance = us)
	# if request.method == 'POST':
	# 	form = forms.UserCreateForm(request.POST, instance=us)
	# 	if form.is_valid():
	# 		form.save()
	# 		return HttpResponseRedirect('/yallaBlog/adminhome/')


	# context = {'us_form': form}
	# return render(request, 'myapp/form.html',context)


def new_badword(request):
	form=badword_form()
	if request.method=='POST':
		form=badword_form(request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect('/yallaBlog/adminlink/adminhome/badword/')
	context={'bad_form':form}
	return render(request,'adminUser/badword_form.html',context)	



def edit_badword(request, id):
	
	qt = badword.objects.get(id= id)
	form = badword_form(instance = qt)
	if request.method == 'POST':
		form = badword_form(request.POST, instance=qt)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect('/yallaBlog/adminlink/adminhome/badword/')
	context = {'bad_form': form}
	return render(request, 'adminUser/badword_form.html',context)




# delete 
def del_badword(request, id):
	dele = badword.objects.get(id=id)
	dele.delete()
	return HttpResponseRedirect('/yallaBlog/adminlink/adminhome/badword/')



def add_comment_to_post(request, id ):
    # post = get_object_or_404(posts)
    post = posts.objects.get(id= id)
    post_id=post.id
    user_id = request.user.id
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post_id = post_id
            comment.author_id=int(user_id)
            comment.check_func()
            comment.save()
            return redirect('/yallaBlog/post/'+id+'/show')
    else:
        form = CommentForm()
    return render(request, 'yallaBlog/add_comment_to_post.html', {'form': form})




def add_reply(request, id , comid ):
    # post = get_object_or_404(posts)
    post = posts.objects.get(id=id)
    # post_id=post.id
    comment=Comment.objects.get(id=comid)
    # comment_id=comment.id
    user_id = request.user.id
    if request.method == "POST":
        form = ReplyForm(request.POST)
        if form.is_valid():
            reply = form.save(commit=False)
            reply.post_id = id
            reply.comment_id= int(comid)
            reply.author_id=int(user_id)
            reply.check_func()
            reply.save()
            return redirect('/yallaBlog/post/'+id+'/show')
    else:
        form = ReplyForm()
    return render(request, 'yallaBlog/replay_comment_.html', {'form': form})






def show_post(request,id):
	post=posts.objects.get(id=id)
	comment=Comment.objects.filter(post_id=id)
	reply=Reply.objects.filter(post_id=id)
	# context={'postshow':post , 'comment' : comment}
	context={'postshow':post , 'comment' : comment, 'reply' : reply}
	return render(request, 'yallaBlog/showpost.html' ,context)



# #@login_required
# def comment_approve(request, pk):
#     comment = get_object_or_404(Comment, pk=pk)
#     comment.approve()
#     return redirect('/yallaBlog/post/'+pk+'/show', pk=comment.post.pk)

# #@login_required
# def comment_remove(request, pk):
#     comment = get_object_or_404(Comment, pk=pk)
#     post_pk = comment.post.pk
#     comment.delete()
#     return redirect('/yallaBlog/post/'+pk+'/show', pk=post_pk)





def adminlink(request):
	all_post = posts.objects.all()
	us = User.objects.all()
	cat = category_table.objects.all()
	bad = badword.objects.all()
	context = {'us_id':us,'cat_id':cat,'bad_id':bad,'all_posts': all_post}
	return render(request, 'adminUser/admin.html',context )
	



def control_category(request):
	cat = category_table.objects.all()
	context = {'cat_id':cat}
	return render(request, 'adminUser/categorydata.html',context)
	

def control_posts(request):
	all_post = posts.objects.all()
	context = {'all_posts': all_post}
	return render(request, 'adminUser/postdata.html',context)



def control_user(request):
	us = User.objects.all()
	context = {'us_id':us}
	return render(request, 'adminUser/userdata.html',context)



def control_badword(request):
	bad = badword.objects.all()
	context = {'bad_id':bad}
	return render(request, 'adminUser/baddata.html',context)