from django.conf.urls import include, url
from django.contrib import admin
from blog import urls 
admin.autodiscover()
urlpatterns = [
    # Examples:
    # url(r'^$', 'blog.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

   	 url(r'^admin/', include(admin.site.urls)),
	url(r'^$','blog.views.home'),
	url(r'^article/',include('blog.urls')),
	url(r'^login/$','blog.views.login'),
	url(r'^accounts/auth/$','blog.views.auth_view'),
	url(r'^accounts/logout/$','blog.views.logout'),
	url(r'^accounts/loggedin/$','blog.views.loggedin'),
	url(r'^accounts/invalid/$','blog.views.invalid'),
	url(r'^accounts/register/$','blog.views.register_user'),
	url(r'^accounts/register_sucess/$','blog.views.register_sucess'),
	url(r'^create/$','blog.views.create'),
	url(r'^accounts/register/$','blog.views.register_user'),
	url(r'^accounts/register_sucess/$','blog.views.register_sucess'),
	url(r'^profile/$','userprofile.views.user_profile'),
	
]
