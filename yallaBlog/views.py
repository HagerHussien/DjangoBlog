from django.contrib.auth.models import User
from django.conf import settings
from django.contrib import messages
from django.core.mail import send_mail
from django.shortcuts import render, redirect 
from django.contrib import auth 
from django.http import HttpResponse,HttpResponseRedirect
from .models import posts,category_table
from forms import post_form,login_form , UserForm

# Create your views here.
# def is_excist (request,form_get):
# 	f = form.cleaned_data['username']
# 	user=User.objects.get(username=f)
# 	if(user):
# 		print "already excists"
# 	else:


def All_category(request):
	all_cat = category_table.objects.all()
	context = {'all_category': all_cat}
	return render(request, 'yallaBlog/category.html' ,context)	


def All_posts(request):
	all_post = posts.objects.all()
	context = {'all_posts': all_post}
	return render(request, 'yallaBlog/index.html' ,context)


def new_post(request):
	form=post_form()
	if request.method=='POST':
		form=post_form(request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect('/yallaBlog/all')
	context={'po_form':form}
	return render(request,'yallaBlog/post_form.html',context)	


def edit_post(request, id):
	
	po = posts.objects.get(id= id)
	form = post_form(instance = po)
	if request.method == 'POST':
		form = post_form(request.POST, instance=po)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect('/yallaBlog/all')



	context = {'po_form': form}
	return render(request, 'yallaBlog/post_form.html',context)




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
	# args={}
	# args.update(csrf(request))
	# args['form']=UserCreationForm()
	# return render_to_response('Blog/register_form.html',args)




# def user_exsict (form):
# 			f = form.cleaned_data['username']
# 			flag=1
# 			try:
# 				of=User.objects.get(username=f)
# 			except User.DoesNotExist :
# 				flag=1
# 			else:
# 				print "already excists"
# 				flag=0
# 			return flag


def loginform(request):
	form=login_form()
	if request.method=='POST':
		form=login_form(request.POST)
		if form.is_valid():
			flag=userlogin_exsict(form)
			if(flag):
				return HttpResponse('invalid')
			else:
				return HttpResponseRedirect('/yallaBlog/register')
	context={'log_form':form}
	return render(request,'yallaBlog/login_form.html',context)	


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



def userlogin_exsict (form):
			u = form.cleaned_data['username']
			p = form.cleaned_data['password']
			flag=1
			try:
				uu=User.objects.get(username=u)
			except User.DoesNotExist :
				flag=1
			else:
				try:
					pp=User.objects.get(password=p)
				except:
					flag=1
				else:
					flag=0
			return flag




