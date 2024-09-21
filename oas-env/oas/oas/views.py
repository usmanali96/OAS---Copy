import email
from django.conf import settings
from django.contrib import messages
from django.shortcuts import render, redirect
import stripe
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
from django.utils.timezone import make_aware
import logging
from django.core.mail import send_mail
from django.utils import timezone
from products.forms import ProductForm
from products.forms import ReviewForm
from django.urls import reverse





#stripe.api_key = settings.STRIPE_SECRET_KEY






#def index(request)
   # return render(request, 'index.html')
def aboutPage(request):
    return render(request, 'about.html')
def register(request):
    return render(request, 'register.html')

def login(request):
    return render(request, 'login.html')


def success(request):
    return render(request, 'success.html')

def cancel(request):
    return render(request, 'cancel.html')






def index(request):
    now = timezone.now()

    # Query to display all products on the page
    productsData = Product.objects.all()

    # Query for products that need emails sent
    productsToEmail = Product.objects.filter(bid_end_time__lte=now, email_sent=False)
    
    for product in productsToEmail:
        if product.bid_end_time is not None:
            target_mili_sec = int(product.bid_end_time.timestamp() * 1000)
            now_mili_sec = int(now.timestamp() * 1000)
            remaining_sec = (target_mili_sec - now_mili_sec) / 1000
            
            if remaining_sec <= 0:
                if product.bids:
                    highest_bid = max(product.bids, key=lambda bid: bid['price'])
                    email = highest_bid.get('email')
                    
                try:
                    if email:
                        send_mail(
                            subject=f'Bid Winner for {product.title}',
                            message=f'Congratulations! You have the highest bid of ${highest_bid["price"]} for {product.title}. Congrats for winning the Auction. We will share the payment details soon.',
                            from_email='onlineauction537@gmail.com',
                            recipient_list=[email],
                        )
                        product.email_sent = True    
                        product.save()
                        logging.info(f"Email sent to {email} for product {product.title}.")
                
                except Exception as e:
                    logging.error(f"Error sending email: {e}")
    

                
            
            

         
    #productsData = Paginator(productsData, 2)
    #page = request.GET['page']
    #products = productsData.get_page(page)

    #1 - loop through thr products to get timing.
    #2 - get target_mili_sec filed for each product
    #3 - calculate the difference var remaining_sec = Math.floor((target_mili_sec - now_mili_sec) / 1000);
    #4 - if the difference is less than zero call the send mailfunction

    #totalPages =[x+1 for x in range (productsData.num_pages)]

    data = {
        "products": productsData,  # Pass all products to the template for display
    }
             
    return render(request, 'index.html', data)







#def checkout(request, product_id):
    # Fetch the product by ID
    product = get_object_or_404(Product, id=product_id)

    # Find the highest bid for the product
    if product.bids:
        highest_bid = max(product.bids, key=lambda bid: bid['price'])
        email = highest_bid.get('email')
        amount = highest_bid.get('price')  # Amount in dollars

    try:
        # Create a Stripe Checkout session
        checkout_session = stripe.checkout.Session.create(
            payment_method_types=['card'],
            line_items=[{
                'price_data': {
                    'currency': 'usd',
                    'product_data': {
                        'name': product.title,  # The product title
                    },
                    'unit_amount': int(amount * 100),  # Convert price to cents (Stripe uses cents)
                },
                'quantity': 1,
            }],
            mode='payment',
            # Success URL: Where to redirect after successful payment
            success_url=request.build_absolute_uri(reverse('success')),
            # Cancel URL: Where to redirect if the user cancels the payment
            cancel_url=request.build_absolute_uri(reverse('cancel')),
        )

        # Redirect to the Stripe payment page
        return redirect(checkout_session.url, code=303)

    except Exception as e:
        # In case of an error, show an error template or message
        return render(request, 'error.html', {'error': str(e)})







#def product_list(request):
  #  query = request.GET.get('q')
  #  if query:
   #     products = Product.objects.filter(title__icontains=query)
   # else:
   #     products = Product.objects.all()
   # return render(request, 'product_list.html', {'products': products})








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

        return render(request, 'register.html')








def loginUser(request):
        uname = request.POST.get('username')
        upassword = request.POST.get('password')
        user = authenticate(request, username=uname, password=upassword)
        if user is not None:
             login(request, user)
             print("User authenticated and logged in.")
             return redirect('index')
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
        message=f'Thank you, {bid["name"]}, for your bid of ${bid["price"]} on {product.title}. Your Bid has been submitted the winner will be announced when the timer ends. If you win the auction we will contact you through email.',
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


    
   

    # Get all products and order them by category

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






#def review_section(request):
   # products = Product.objects.filter(category='client-review')

  #  if request.method == 'POST':
  #      form = ReviewForm(request.POST)
   #     if form.is_valid():
    #        product = Product.objects.get(id=request.POST.get('product_id'))

            # Save the form data into the model fields
    #        product.title = form.cleaned_data['name']
    #        product.description = form.cleaned_data['comment']
    #        product.save()

    #        return redirect('review_section')
 #   else:
 #       form = ReviewForm()

 #   return render(request, 'your_template.html', {'products': products, 'form': form})




def add_review(request):
    if request.method == 'POST':
        form = ReviewForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = ReviewForm()

    return render(request, 'add_review.html', {'form': form})




def add_product_view(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)  
        if form.is_valid():
            form.save()
            messages.success(request, 'Your product has been successfully added!')  
            return redirect('add_product')  
    else:
        form = ProductForm()

    return render(request, 'add_product.html', {'form': form})






def shop_page(request):
    
    productsData = Product.objects.all()
    data = {
        "products": productsData,  # Pass all products to the template for display
    }
             
    return render(request, 'shop.html', data)

