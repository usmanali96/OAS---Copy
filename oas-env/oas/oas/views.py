from django.contrib import messages
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
    if request.method == 'POST':
        uname = request.POST.get('username')
        uemail = request.POST.get('email')
        upassword = request.POST.get('password')

        if not uname or not uemail or not upassword:
            messages.error(request, "All fields are required.")
            return render(request, 'register.html')
        
        try:
            user = User.objects.create_user(username=uname, email=uemail, password=upassword)
            messages.success(request, "Registration successful.")
            return redirect('login')  # Redirect to the login page or another appropriate page
        except Exception as e:
            messages.error(request, f"An error occurred: {str(e)}")
            return render(request, 'register.html')
    else:
        return render(request, 'register.html')
