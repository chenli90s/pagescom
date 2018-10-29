from .base import models, BaseModel


class Contacts(BaseModel):

    name = "我们的信息"
    more = False

    公司地址 = models.CharField(max_length=255)
    电话号码 = models.CharField(max_length=255)
    电子邮件 = models.CharField(max_length=255)
    信息描述 = models.CharField(max_length=255)


class Maps(BaseModel):
    name = "地图位置分享"
    more = False

    分享链接 = models.CharField(max_length=255)