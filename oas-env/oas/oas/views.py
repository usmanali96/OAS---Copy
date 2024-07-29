from django.shortcuts import render
from django.contrib.auth.models import User

def index(request):
    return render(request, 'index.html')
def aboutPage(request):
    return render(request, 'about.html')
def register(request):
    return render(request, 'register.html')


def registerUser(request):
    uname = request.POST('username')
    uemail = request.POST('email')
    upassword = request.POSt('password')

    user = User.objects.create_user(username=uname, email=uemail, password=upassword)
    return render(request, 'register.html')