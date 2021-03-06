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
        def inner(request, **kwargs):
            # print(kwargs, '+++++++++++++++++=')
            params = func(request, **kwargs)
            g = GlobalModel.objects.all()[0]
            cates = OurProductCate.objects.all()
            params['g'] = g
            params['cates'] = cates
            return render(request, tp, params)
        return inner
    return wrapper


# Create your views here.
@tplt('home.html')
def home(request):
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

@tplt("service.html")
def service(request):
    ourGuidancess = OurGuidances.objects.all()
    ourAdvantages = OurAdvantage.objects.all()
    return dict(ourGuidancess=ourGuidancess, ourAdvantages=ourAdvantages)

@tplt('product.html')
def product(request, cate):
    products = OurProduct.objects.filter(产品分类=cate)
    return dict(cate=cate, products=products)

@tplt('contact.html')
def contact(request):
    contacts = Contacts.objects.all()
    maps = Maps.objects.all()
    return dict(contacts=contacts, maps=maps)

@tplt('login.html')
def login(request):
    return dict()

@tplt('register.html')
def register(request):
    return dict()


@tplt('detail.html')
def detail(request, name):
    products = OurProduct.objects.filter(产品名字=name)
    if len(products)>0:
       return dict(products=products[0])
    return dict(products=products)