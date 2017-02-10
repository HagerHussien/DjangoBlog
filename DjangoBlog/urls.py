"""DjangoBlog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url,include
from django.contrib import admin
#from moments_app.views import *
#from yallaBlog.views import *
#from django.contrib.auth import views
#from yallaBlog.forms import login_form
#from yallaBlog.views import index

#from moments_app import views
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^yallaBlog/',include('yallaBlog.urls')),
    url(r'^logout/$', 'django.contrib.auth.views.logout',
                          {'next_page': '/yallaBlog/home'}),
    url(r'^$' , include('yallaBlog.urls'))
    #url(r'^login/$', views.login, {'template_name': 'login_form.html', 'authentication_form': login_form}, name='login'),

    # #user register 
    # url(r'^yallaBlog/register/$' , yallaBlog.views.register_user),
    # url(r'^yallaBlog/register_success/$' , yallaBlog.views.register_success),
]
