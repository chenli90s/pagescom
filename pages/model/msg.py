from .base import models



class Price(models.Model):


    name = "咨询报价"

    more = True

    称呼 = models.CharField(max_length=255,null=True, blank=True, )
    电子邮件 = models.CharField(max_length=255,null=True, blank=True, )
    地址 = models.CharField(max_length=255,null=True, blank=True, )
    咨询目的 = models.CharField(max_length=255,null=True, blank=True, )
    咨询产品 = models.CharField(max_length=255,null=True, blank=True, )
    联系电话 = models.CharField(max_length=255,null=True, blank=True, )
    已读 = models.BooleanField(default=False)


class Message(models.Model):


    name = "发送消息"

    more = True

    全名 = models.CharField(max_length=255,null=True, blank=True, )
    电子邮件 = models.CharField(max_length=255,null=True, blank=True, )
    网站 = models.CharField(max_length=255,null=True, blank=True, )
    你的消息 = models.CharField(max_length=255,null=True, blank=True, )
    已读 = models.BooleanField(default=False)


