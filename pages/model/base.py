from django.db import models

class BaseModel(models.Model):

    # 是否展示
    ishow = models.BooleanField(default=True)
    # 图片
    image = models.ImageField(null=True, blank=True)

    class Mate:
        abstract = True