from django.shortcuts import render
from django.http import HttpResponse
from blog.models import Article
from django.shortcuts import render_to_response
from django.core.context_processors import csrf
from django.http import HttpResponseRedirect
from django.contrib import auth
from django.contrib.auth.forms import UserCreationForm
from blog.forms import MyForm
from blog.forms import  RegistrationForm

# Create your views here.
def home(request):
	return HttpResponse("this is our home page")

def articles(request):
	return render_to_response('articles.html',{'articles':Article.objects.all()})
def article(request,article_id=1):
	return render_to_response('article.html',{'article':Article.objects.get(id=article_id)})
def login(request):
	c={}
	c.update(csrf(request))
	return render_to_response('login.html',c)
def auth_view(request):
	username=request.POST.get('username','')
	password=request.POST.get('password','')
	user=auth.authenticate(username=username,password=password)
	if user is not None:
		auth.login(request,user)
		
		return HttpResponseRedirect('/accounts/loggedin')
	else:
		return  HttpResponseRedirect('/accounts/invalid')

def loggedin(request):
	name=request.user.username
	return render_to_response('loggedin.html',{'full_name':name})
def logout(request):
	auth.logout(request)
	return render_to_response('logout.html')
def invalid(request):
	return render_to_response('invalid.html')
def register_user(request):
	if request.method=="POST":
		form=MyForm(request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect('/accounts/register_sucess/')
	args={}
	args.update(csrf(request))
	args['form']=MyForm
	return render_to_response('register.html',args)
	
def register_sucess(request):
	return render_to_response('register_sucess.html')
def create(request):
	if request.method=="POST":
		form= RegistrationForm(request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect('/article/all/')
	args={}
	args.update(csrf(request))
	args['form']= RegistrationForm
	return render_to_response('create_article.html',args)
	

