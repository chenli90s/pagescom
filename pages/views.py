from django.shortcuts import render
from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, "home.html")


def about(request):
    return render(request, "about.html")


def service(request):
    return render(request, "service.html")

def product(request):
    return render(request, 'product.html')

def contact(request):
    return render(request, 'contact.html')

def login(request):
    return render(request, 'login.html')

def register(request):
    return render(request, 'register.html')