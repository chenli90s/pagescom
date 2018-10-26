from django.db import models

class BaseModel(models.Model):

    # 是否展示
    是否展示 = models.BooleanField(default=True)
    # 图片
    上传图片 = models.ImageField(null=True, blank=True, upload_to="static/imgs")

    class Mate:
        abstract = True