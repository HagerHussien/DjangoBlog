from django.contrib.auth.models import User 
from django import forms
from .models import posts,category_table , badword,Comment , Reply 
from django.forms import  Textarea,ChoiceField,PasswordInput
from django.contrib.auth.forms import AuthenticationForm , UserCreationForm


class UserCreateForm(UserCreationForm):
	class Meta:
		model = User
		fields = ('username', 'email','password1','password2')

	def __init__(self,*args, **kwargs):
		super(UserCreateForm, self).__init__(*args, **kwargs)
	def clean_email(self):
	        clean_data = super(UserCreateForm, self).clean()
	        email=clean_data.get('email')
	        if User.objects.filter(email=email).count() > 0:
	            raise forms.ValidationError("this email is already in use")
	        print("clean_email")
	        return email

class UserForm(forms.ModelForm):
	password = forms.CharField(widget=forms.PasswordInput)
	class Meta:
		model = User
		fields = ('username', 'email','password')


class post_form(forms.ModelForm):
    
	class Meta:
		GENDER = ((1,('Mr.')),(2,('Ms.')))
		model = posts
		fields = ('title','post','cat')
		widgets = {'post': Textarea(attrs={'cols': 60, 'rows': 10})} 
		category = forms.ChoiceField(choices=GENDER)


class login_form(forms.ModelForm):
	password = forms.CharField(widget=forms.PasswordInput) 
	class Meta:		
		model = User
		fields = ('username','password')
        
		#widgets = {'password': forms.HiddenInput()} -> for hidden an attribute
            	

#class UploadFileForm(forms.Form):
    
    #image  = forms.FileField()


class category_form(forms.ModelForm):
	class Meta:		
		model = category_table
		fields = ('name',)

class badword_form(forms.ModelForm):
	class Meta:		
		model = badword
		fields = ('rude_word',)




# class CommentForm(forms.ModelForm):

#     class Meta:
#         model = Comment
#         fields = ('author', 'text',)

class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ( 'text',)



class ReplyForm(forms.ModelForm):

    class Meta:
        model = Reply
        fields = ( 'text',)