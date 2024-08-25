from django.contrib import messages
from django.shortcuts import render, redirect
from products.models import Products
from django.contrib.auth.models import User
from django.core.paginator import Paginator
from django.contrib.auth import authenticate, login
from contact.models import Contact
from django import forms
from django.contrib.auth.forms import UserCreationForm
from contact.forms import contactForm
from contact.models import Contact  
from datetime import datetime


#def index(request):
   # return render(request, 'index.html')
def aboutPage(request):
    return render(request, 'about.html')
def register(request):
    return render(request, 'register.html')

def login(request):
    return render(request, 'login.html')




def  index(request):

    productsData = Products.objects.all()
    #productsData = Paginator(productsData, 2)
    #page = request.GET['page']
    #products = productsData.get_page(page)


    #totalPages =[x+1 for x in range (productsData.num_pages)]

    data = {
        "products":  productsData,
        #"totalPages":totalPages,
        }
             
    return render(request, 'index.html', data)

def my_view(request):
    products = [
        {"id": 1, "category": "1st-Auction", "countdown_date": "2024-08-30T15:00:00"},
        {"id": 2, "category": "1st-Auction", "countdown_date": "2024-09-01T12:00:00"},
        # Add more products as needed
    ]
    return render(request, 'my_template.html', {'products': products})



def registerUser(request):
        uname = request.POST.get('username')
        uemail = request.POST.get('email')
        upassword = request.POST.get('password')
        user = User.objects.create_user(username=uname, email=uemail, password=upassword)

        return render(request, 'register.html')




def loginUser(request):
        uname = request.POST.get('username')
        upassword = request.POST.get('password')
        user = authenticate(request, username=uname, password=upassword)
        if user is not None:
             login(request)
             return redirect('/')
        else:
             print("user doesn't exist")
             
        return render(request, 'login.html')
             



def contactPage(request):
    if request.method == 'POST':
        form = contactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('contact')  # Redirect to a success page or another URL after submission
    else:
        form = contactForm()

    return render(request, 'contact.html', {"form": form})
