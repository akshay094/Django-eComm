from django.shortcuts import render,redirect
from .models import Products
# from django.contrib.auth.models import User,auth

# Create your views here.
def homepage(request):
  prod = Products.objects.all();
  return render(request ,'homePage.html' , {"prod":prod});

def login(request):
  if(request.method == 'POST'):
    pass
  else:
    return render(request , 'login.html')


def signup(request):
  if(request.method == 'POST'):
    username = request.post.get('username');
    firstname = request.post.get('firstname');
    lastname = request.post.get('lastname');
    password = request.post.get('password');
    # user=User.objects.create_user(username=username,first_name=firstname,last_name=lastname,password=password,email=email)
  else:
    return render(request , 'signup.html')