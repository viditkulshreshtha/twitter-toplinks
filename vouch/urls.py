from django.contrib import admin
from django.urls import path
from twitterapp import views
from django.conf.urls import url  
urlpatterns = [
    path('admin/', admin.site.urls),
    url('', views.homeview, name='home'),
    url(r'^username/$', views.usernamereq, name='username'),
    url(r'^tweets/$', views.tweets, name='tweets'), 
    url(r'^friendtweets/$', views.friendstweet, name='friendstweet'),       



]
