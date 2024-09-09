from django.contrib import messages
from django.shortcuts import render, redirect
from products.models import Product
from django.contrib.auth.models import User
from django.core.paginator import Paginator
from django.contrib.auth import authenticate, login
from contact.models import Contact
from django import forms
from django.contrib.auth.forms import UserCreationForm
from contact.forms import contactForm
from contact.models import Contact  
from datetime import datetime
from django.contrib import admin
from django.shortcuts import render, get_object_or_404, redirect
from products.models import Product
from django.core.mail import send_mail
from datetime import datetime, timedelta
from django.template.loader import render_to_string
from django.core.mail import EmailMessage




#def index(request)
   # return render(request, 'index.html')
def aboutPage(request):
    return render(request, 'about.html')
def register(request):
    return render(request, 'register.html')

def login(request):
    return render(request, 'login.html')

def cartPage(request):
    return render(request, 'cart.html')






def  index(request):

    productsData = Product.objects.all()
    #productsData = Paginator(productsData, 2)
    #page = request.GET['page']
    #products = productsData.get_page(page)


    #totalPages =[x+1 for x in range (productsData.num_pages)]

    data = {
        "products":  productsData,
        #"totalPages":totalPages,
        }
             
    return render(request, 'index.html', data)









def product_detail(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    return render(request, 'product_detail.html', {'product': product})





#def my_view(request):
#    products = [
 #       {"id": 1, "category": "1st-Auction", "countdown_date": "2024-08-30T15:00:00"},
  #      {"id": 2, "category": "1st-Auction", "countdown_date": "2024-09-01T12:00:00"},
  #      # Add more products as needed
  #  ]
   # return render(request, 'index.html', {'products': products})



#def registerUser(request):
 #       uname = request.POST.get('username')
  #      uemail = request.POST.get('email')
   #     upassword = request.POST.get('password')
    #    user = User.objects.create_user(username=uname, email=uemail, password=upassword)

     #   return render(request, 'register.html')


def registerUser(request):
    if request.method == 'POST':
        uname = request.POST.get('username')
        uemail = request.POST.get('email')
        upassword = request.POST.get('password')

    
        User.objects.create_user(username=uname, email=uemail, password=upassword)

       
        return redirect('login') 

    return render(request, 'register.html')



def loginUser(request):
        uname = request.POST.get('username')
        upassword = request.POST.get('password')
        user = authenticate(request, username=uname, password=upassword)
        if user is not None:
             login(request, user)
             print("User authenticated and logged in.")
             return redirect('/')
        else:
              print("User authentication failed.")
             
        return render(request, 'login.html')
             



def contactPage(request):
    if request.method == 'POST':
        form = contactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('contact') 
    else:
        form = contactForm()

    return render(request, 'contact.html', {"form": form})





def send_bid_end_email(product, bid):
       send_mail(
        subject=f'New Bid Received for {product.title}',
        message=f'Thank you, {bid["name"]}, for your bid of {bid["price"]} on {product.title}. Your Bid has been submitted the winner will be announced when the timer ends. If you win the auction we will contact you through email.',
        from_email='onlineauction537@gmail.com',
        recipient_list=[bid["email"]],
       )

def save_price(request, product_id):
    
    
    product = get_object_or_404(Product, id=product_id)
    
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        price = request.POST.get('price')

        
        new_bid = {
            'name': name,
            'email': email,
            'price': price,
        }

        product.bids.append(new_bid)
        product.save()


        send_bid_end_email(product, new_bid)

        messages.success(request, 'Your bid has been successfully submitted!')


        return redirect('product_detail', product_id=product_id)
    
    return render(request, 'product_detail.html', {'product': product})





def browse_page(request):
    
    productsData = Product.objects.all().order_by('category', 'id')  # Ordering by category, then by id

    bot = Paginator(productsData, 10) 
    page_number = request.GET.get('page', 1)
    page_obj = bot.get_page(page_number)

    totalpages = [x + 1 for x in range(bot.num_pages)]
    
    data = {
        "products": page_obj,
        "totalPages": totalpages
    }

    return render(request, 'browse_product.html', data)