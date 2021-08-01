from django.shortcuts import render,redirect
from .models import Products
from django.contrib import messages
from django.contrib.auth.models import User , auth
# from django.contrib.auth.models import User,auth

# Create your views here.
def homepage(request):
  prod = Products.objects.all();
  return render(request ,'homePage.html' , {"prod":prod});

def login(request):
  if(request.method == 'POST'):
    username = request.POST['username']
    password = request.POST['password']

    user = auth.authenticate(username=username, password=password)
    if user is not None:
        auth.login(request , user)
        return redirect('/')
  else:
    messages.info(request , "Login Successfull!")
    return render(request , 'login.html')


def signup(request):
  if(request.method == 'POST'):
    username = request.POST.get('username');
    firstname = request.POST.get('firstname');
    lastname = request.POST.get('lastname');
    password = request.POST.get('password');
    user=User.objects.create_user(username=username,first_name=firstname,last_name=lastname,password=password)
    user.save()
    return redirect('/')
  else:
    messages.info(request ,"Signup Successful!")
    return render(request , 'signup.html')

def cartpage(request):
  ide = request.POST['id']
  ide = int(ide)
  obj = Products.objects.filter(id=ide)
  if(request.method == "POST"):
    return render(request , 'cart.html' , {"obj":obj})

def logout(request):
  auth.logout(request)
  messages.info(request , "Logged Out")
  return redirect('/')
    
