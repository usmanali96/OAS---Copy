from django.shortcuts import render, redirect
from products.models import Products
from django.contrib.auth.models import User
from django.core.paginator import Paginator

def index(request):
    return render(request, 'index.html')
def aboutPage(request):
    return render(request, 'about.html')
def register(request):
    return render(request, 'register.html')

def login(request):
    return render(request, 'login.html')




def  home(request):

    productsData = Products.objects.all()
    products = Paginator(productsData, 2)
    page = request.GET['page']
    products = products.get_page(page)

    data = {
        "products":  productsData,
        }
             
    return render(request, 'home.html', data)









def registerUser(request):
    uname = request.POST['username']
    uemail = request.POST['email']
    upassword = request.POST['password']

    user = User.objects.create_user(username=uname, email=uemail, password=upassword)
    return render(request, 'register.html')

