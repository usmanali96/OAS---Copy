from django.shortcuts import render, redirect
from products.models import Products
from django.contrib.auth.models import User
from django.core.paginator import Paginator

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
    uname = request.POST['username']
    uemail = request.POST['email']
    upassword = request.POST['password']

    user = User.objects.create_user(username=uname, email=uemail, password=upassword)
    return render(request, 'register.html')

