
from django.contrib.auth import views as auth_views
from django.conf.urls import url
from django.contrib import admin
import views

urlpatterns = [
# url(r'^mail$',views.send_email),
url(r'^$',views.homePosts),
url(r'^register/$',views.register.as_view(),name="register"),
url(r'^login$' , views.custom_login , name="login"),  
#url(r'^login$' ,views.auth_view),
url(r'^all$' , views.All_posts),
url(r'^new$' , views.new_post),
url(r'^edit/(?P<id>[0-9]+)/post$' , views.edit_post),
#url(r'^register$' , views.registerForm),
# url(r'^home/$' , views.top_post ),
url(r'^logout/$' ,auth_views.logout, {'next_page': '/admin'}, name='logout'),
#url(r'^home$' , views.All_category),
#url(r'^home$' , views.home),
#url(r'^cat/(?P<id>[0-9]+)/post$' , views.cat_posts),
url(r'^post/(?P<id>[0-9]+)/show$' , views.show_post),
# url(r'^post/(?P<id>[0-9]+)/(?P<pk>[0-9]+)/comment$', views.add_comment_to_post, name='add_comment_to_post'),
url(r'^post/(?P<id>[0-9]+)/comment$', views.add_comment_to_post, name='add_comment_to_post'),
url(r'^post/(?P<id>[0-9]+)/(?P<comid>[0-9]+)/reply$', views.add_reply, name='add_reply'),
# url(r'^comment/(?P<pk>\d+)/approve/$', views.comment_approve, name='comment_approve'),
# url(r'^comment/(?P<pk>\d+)/remove/$', views.comment_remove, name='comment_remove'),

#subscribe
url(r'^home/subscribe/(?P<cat_id>[0-9]+)$', views.subscribe ),
url(r'^home/$', views.homePosts ),
url(r'^home/unsubscribe/(?P<cat_id>[0-9]+)$', views.unsubscribe ),



#subscribe from category page
url(r'^cat/subscribe/(?P<cat_id>[0-9]+)$', views.subscribeCAT ),
url(r'^cat/(?P<cat_id>[0-9]+)/post$', views.homePostsCAT ),
url(r'^cat/unsubscribe/(?P<cat_id>[0-9]+)$', views.unsubscribeCAT ),




#admin_affect_user
#url(r'^adminlink/adminhome/$' , views.adminhome , name='adminHome'),
url(r'^adminlink/adminhome/user/(?P<us_id>[0-9]+)/details$' , views.details_user ),
url(r'^adminlink/adminhome/user/new$' ,views.registerFromAdmin.as_view(),name="registerFromAdmin"),
url(r'^adminlink/adminhome/user/(?P<us_id>[0-9]+)/delete$' , views.del_user),
#url(r'^adminlink/adminhome/user/(?P<us_id>[0-9]+)/edit$' ,views.edit_user.as_view(),name="editUser"),
url(r'^adminlink/adminhome/user/(?P<pk>[0-9]+)/edit$' ,views.edit_user.as_view(),name="edituser"),

#admin_affect_category
#url(r'^adminhome/$' , views.adminhome , name='adminHome'),
#url(r'^adminhome/category/(?P<cat_id>[0-9]+)/details$' , views.category),
#url(r'^adminhome/category/new$' ,views.registerFromAdmin.as_view(),name="registerFromAdmin"),
url(r'^adminlink/adminhome/category/(?P<cat_id>[0-9]+)/delete$' , views.del_category),
url(r'^adminlink/adminhome/category/new$' , views.new_category),
url(r'^adminlink/adminhome/category/(?P<cat_id>[0-9]+)/edit$' , views.edit_category),


#admin_affect_badwords
#url(r'^allb$' , views.All_badword),
url(r'^adminlink/adminhome/badword/new$' , views.new_badword),
url(r'^adminlink/adminhome/badword/(?P<id>[0-9]+)/edit$' , views.edit_badword),
url(r'^adminlink/adminhome/badword/(?P<id>[0-9]+)/delete$' , views.del_badword),

url(r'^adminlink/adminhome/post/new$', views.new_post),
url(r'^adminlink/adminhome/post/(?P<id>[0-9]+)/edit$' , views.edit_post),
url(r'^adminlink/adminhome/post/(?P<id>[0-9]+)/delete$' , views.del_post),
url(r'^adminlink/adminhome/post/(?P<id>[0-9]+)/details$' , views.details_post),


url(r'^adminlink/$' , views.adminlink , name='adminLink'),
url(r'^adminlink/adminhome/category/$' , views.control_category),
url(r'^adminlink/adminhome/post/$' , views.control_posts),
url(r'^adminlink/adminhome/user/$' , views.control_user , name='adminHome'),
url(r'^adminlink/adminhome/badword/$' , views.control_badword),


]

