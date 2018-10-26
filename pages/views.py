from django.shortcuts import render
from django.shortcuts import render
from .model.service import *
from .model.home import *
from .model.about import *
from .model.contact import *
from .model.product import *
from .models import *

def tplt(tp):
    def wrapper(func):
        def inner(request):
            params = func()
            g = GlobalModel.objects.all()[0]
            params['g'] = g
            return render(request, tp, params)
        return inner
    return wrapper


# Create your views here.
@tplt('home.html')
def home():
    sliders = Slider.objects.all()
    service = OurService.objects.all()
    choiceus = Choiceus.objects.all()
    news = News.objects.all()
    comment = Comment.objects.all()
    return dict(sliders=sliders, services=service, choiceus=choiceus, news=news, comment=comment)


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