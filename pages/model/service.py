from .base import models, BaseModel


class OurGuidances(BaseModel):

    name = "我们的指导"

    more = True

    图标 = models.CharField(max_length=255,null=True, blank=True, )
    服务类型 = models.CharField(max_length=255,null=True, blank=True, )
    指导描述 = models.CharField(max_length=255,null=True, blank=True, )


class OurAdvantage(BaseModel):

    name = "我们的优点"

    more = True


    优点描述 = models.CharField(max_length=255,null=True, blank=True, )
    优点分类 = models.CharField(max_length=255,null=True, blank=True, )


