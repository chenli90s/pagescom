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

    口号 = models.CharField(max_length=255)

    服务类型 = models.CharField(max_length=255)
    服务描述 = models.CharField(max_length=255)


class Choiceus(BaseModel):

    name = "为什么选择我们"

    more = True

    选择原因 = models.CharField(max_length=255)
    选择原因标题 = models.CharField(max_length=255)


class News(BaseModel):

    name = "最新消息"

    more = True

    消息内容 = models.CharField(max_length=255)
    消息标题 = models.CharField(max_length=255)


class Comment(BaseModel):

    name = "客户评价"

    more = True


    客户头像 = models.CharField(max_length=255)
    客户姓名 = models.CharField(max_length=255)
    客户职位 = models.CharField(max_length=255)
    客户描述 = models.CharField(max_length=255)


class Clients(BaseModel):

    name = "客户"

    more = True