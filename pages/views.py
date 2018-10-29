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
    clients = Clients.objects.all()
    return dict(sliders=sliders, services=service, choiceus=choiceus, news=news, comments=comment, clients=clients)

@tplt('about.html')
def about(request):
    ourGuidances = OurGuidance.objects.all()
    ourGoods = OurGood.objects.all()
    ourTeams = OurTeam.objects.all()
    ourPartners = OurPartners.objects.all()
    return dict(ourGuidances=ourGuidances, ourGoods=ourGoods, ourTeams=ourTeams, ourPartners=ourPartners)


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