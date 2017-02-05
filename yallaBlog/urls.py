

from django.conf.urls import url
import views

urlpatterns = [
   
url(r'^login$' , views. loginform),
url(r'^all$' , views.All_posts),
url(r'^new$' , views.new_post),
url(r'^edit/(?P<id>[0-9]+)/post$' , views.edit_post),
url(r'^register$' , views.registerForm),
url(r'^home$' , views.All_category),



]
