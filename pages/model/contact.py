from .base import models, BaseModel


class Contacts(BaseModel):

    name = "我们的信息"
    more = False

    公司地址 = models.CharField(max_length=255)
    电话号码 = models.CharField(max_length=255)
    电子邮件 = models.CharField(max_length=255)