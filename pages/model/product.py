from .base import models, BaseModel




class OurProduct(BaseModel):

    name = "产品类别名称"

    more = True

    产品名字 = models.CharField(max_length=255)
    产品价格 = models.CharField(max_length=255)
	# 产品评级 = models.CharField(max_length=255)

