from django.shortcuts import render

def index(request):
    return render(request, 'index.html')
def aboutPage(request):
    return render(request, 'about.html')