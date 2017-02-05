from django.contrib.auth.models import User 
from django import forms
from .models import posts
from django.forms import  Textarea,ChoiceField,PasswordInput




class UserForm(forms.ModelForm):
	password = forms.CharField(widget=forms.PasswordInput)
	class Meta:
		model = User
		fields = ('username', 'email','password')


class post_form(forms.ModelForm):
    
	class Meta:
		GENDER = ((1,('Mr.')),(2,('Ms.')))
		model = posts
		fields = ('title','post','category','comment')
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






