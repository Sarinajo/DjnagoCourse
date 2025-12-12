#i created this
'''{% comment %}
when we do install django

and do django-admin, it gives subcommands that we can use.
one of them is startproject. we can use startproject to start our project
when we do django-admin startproject projectname
a project is created of the project name
projectname
	projectname
		manage.py

manage.py is a command line utility. it helps to interact with django project

when we do
	 python3 manage.py runserver
the server runs


django view
 it is a python function that recieves web request and returns web reposne.
every view must return HttpResponse object

the it should be connected to URLs

in urls.py, add the path that will lead to view
path(route, view, kwargs=none, name=none)

foreg in views.py we have
def index(request):
	return Httpresponse(‘hello)

in urls.py

in urlpatterns = [
path(‘’, views.index, name = ‘index’)



]
views can be written in class too instead of function. also Class based Views also known as CBV.
CBV inherits from django.views.View

class HomeView(view):
	def get(self, request):
		return HttpResoonse("hello")
in in yrls.py we write
path('',HomeView.as_view(),name ='home')
'''



from django.views import View
from django.http import HttpResponse
from django.shortcuts import render
import os


def index(request):
	context = {'name':'Sarina'}
	return render(request, 'index.html', context)
    #return HttpResponse('''<h1>Hello SJ</h1> <a href="https://www.youtube.com/watch?v=AepgWsROO4k&list=PLu0W_9lII9ah7DDtYtflgwMwpT3xmjXY9&index=7"> Django Code with harry <a/>''')

def about(request):
	return HttpResponse('''<h1>This is about page</h1> <a href="/"><button>Go back to home page</button></a>''')

def fileo(request):
	file_dir = os.path.dirname(__file__)
	file_path = os.path.join(file_dir,'one.txt')
	with open(file_path,'r') as f:
		content = f.read()
		return HttpResponse(content)

def home(request):
	return HttpResponse('''<h1>This is home page</h1> <a href="/about/"><button>Go to about page</button></a>''')



