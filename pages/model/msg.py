from .base import models



class Price(models.Model):


    name = "咨询报价"

    more = True

    称呼 = models.CharField(max_length=255)
    电子邮件 = models.CharField(max_length=255)
    地址 = models.CharField(max_length=255)
    咨询目的 = models.CharField(max_length=255)
    咨询产品 = models.CharField(max_length=255)
    联系电话 = models.CharField(max_length=255)
    已读 = models.BooleanField(default=False)


class Message(models.Model):


    name = "发送消息"

    more = True

    全名 = models.CharField(max_length=255)
    电子邮件 = models.CharField(max_length=255)
    网站 = models.CharField(max_length=255)
    你的消息 = models.CharField(max_length=255)
    已读 = models.BooleanField(default=False)


