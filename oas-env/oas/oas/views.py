from django.contrib import messages
from django.shortcuts import render, redirect
from products.models import Products
from django.contrib.auth.models import User
from django.core.paginator import Paginator
from django.contrib.auth import authenticate, login

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
             
        return render(request, 'login')
             

