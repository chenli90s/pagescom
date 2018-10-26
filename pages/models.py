from django.db import models
from .model.home import *
from .model.about import *
from .model.product import *
from .model.service import *
from .model.contact import *
# Create your models here.



class GlobalModel(models.Model):

    name = '全局设置'

    more = False

    logo = models.ImageField(null=True, blank=True, upload_to="static/imgs")

    标题 = models.CharField(max_length=255)

    地址 = models.CharField(max_length=255)

    邮箱 = models.CharField(max_length=255)

    电话 = models.CharField(max_length=255)

    手机 = models.CharField(max_length=255)

    关于我们 = models.CharField(max_length=255)

    微信 = models.CharField(max_length=255, blank=True)

    微博 = models.CharField(max_length=255, blank=True)

    QQ = models.CharField(max_length=255, blank=True)

    淘宝 = models.CharField(max_length=255, blank=True)
