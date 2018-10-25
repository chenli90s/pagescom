from .base import models, BaseModel


class Slider(BaseModel):

    # 模块名称
    name = "轮播图"
    # 该模块里面是否多个条目
    more = False

    口号 = models.CharField(max_length=255)

    响亮口号 = models.CharField(max_length=255)

    使命 = models.CharField(max_length=255)


class OurService(BaseModel):

    name = "我们的服务"

    more = True

    服务类型 = models.CharField(max_length=255)
    服务描述 = models.CharField(max_length=255)