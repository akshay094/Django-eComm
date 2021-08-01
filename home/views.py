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
    username = request.POST.get('username');
    firstname = request.POST.get('firstname');
    lastname = request.POST.get('lastname');
    password = request.POST.get('password');
    # user=User.objects.create_user(username=username,first_name=firstname,last_name=lastname,password=password,email=email)
  else:
    return render(request , 'signup.html')

def cartpage(request):
  ide = request.POST['id']
  ide = int(ide)
  obj = Products.objects.filter(id=ide)
  if(request.method == "POST"):
    return render(request , 'cart.html' , {"obj":obj})
  else:
    return render(request , 'cart.html')

    
