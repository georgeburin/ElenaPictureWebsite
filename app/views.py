from django.shortcuts import render, redirect #allow us to redirect the user into another page
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.http import HttpResponse, Http404

from app.models import Picture 

# Create your views here. Everything below is our code. 

# pip install django      install django in the computer
# pip install virtualenvwrapper-win               now we need a virtual environment
# mkvirtualenv myapp2              creates and activates a virtual environment. (myapp) C:\Users\georg>
#         now we are in vm called myapp2 (should be the same as project name!!!)
# pip install django      install django in the virtual environment once you are there
# django-admin startproject myapp2     create a project. THIS IS A PROJECT. there should be only 1 project
# p
# deactivate - gets you out of the virtual env
# workon myapp - this is how you get into the vm
# go to the root directory where manage.py is located and:
# python manage.py startapp myapp2 - THIS CREATES AN APP. there can be many apps within one project. like news feed is one app in project INSTAGRAM, marketplace is another
# python manage.py runserver

#python manage.py makemigrations     - do this every time you make changes to models.py
#python manage.py migrate

#python manage.py createsuperuser    - creates admin user to the .../admin

#postgresql, pgadmin4 need to download from internet if you want to have relational database (SQL database)
#open pgadmin and create a new database named myproject
#go to settings of this django project and where it says DATABASES put all the things that are needed
#pip install psycopg2
#pip install Pillow    -libraries used to connect postgresql to django
#python manage.py makemigrations but before that put the password for the database in settings
#python manage.py migrate

def index(request):
  #return HttpResponse('<h1>Hey, Welcome</h1>') #but how do we render an html file?
  return render(request, 'index.html')

def pictures(request):
  pics=Picture.objects.all()
  return render(request, 'pictures.html', {'pics':pics})

def about(request):
  return render(request, 'about.html')







#garbage code below. not for this project. its a reference

def register(request):
  if request.method == "POST":
    username = request.POST['username']
    email = request.POST['email']
    password = request.POST['password']
    password2 = request.POST['password2']

    if password == password2:
      if User.objects.filter(email=email).exists(): #check if email already exists in the database
        messages.info(request, "Email Already Used") #send a responce back because there is an error
        return redirect('register') #user would have to go through the form above again and type in different email 
      elif User.objects.filter(username=username).exists(): 
        messages.info(request, "Username Already Used")
        return redirect('register')
      else: #if everything is good above then
        user = User.objects.create_user(username=username, email=email, password=password)
        user.save()
        return redirect('login') #redirecting user to the login page
    else: #if passwords dont match
      messages.info(request, 'Password Not The Same')
      return redirect('register')
  else:
    return render(request, 'register.html')
  
def login(request):
  if request.method == 'POST':
    username = request.POST['username']
    password = request.POST['password']

    user = auth.authenticate(username=username,password=password)

    if user is not None: #this means if the user exists on our platform
      auth.login(request, user)
      return redirect('/')
    else:
      messages.info(request, 'Credentials Invalid')
      return redirect ('login')
  else:
    return render (request, 'login.html') 
   
def logout(request):
  auth.logout(request)
  return redirect('/')

def counter(request):
  posts = [1,2,3,4,5,'tim','tom','john']
  return render(request, 'counter.html', {'posts': posts})

def post(request, pk): #passing a variable named pk
  return render(request, 'post.html', {'pk':pk})
