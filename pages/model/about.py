from .base import models, BaseModel

class OurGuidance(BaseModel):

    name = "我们的业务"

    more = True

    业务类型 = models.CharField(max_length=255)
    业务描述 = models.CharField(max_length=255)


class OurGood(BaseModel):

    name = "我们的经验"

    more = False


    擅长的领域描述 = models.CharField(max_length=255)
    擅长的领域分类 = models.CharField(max_length=255)


class OurTeam(BaseModel):

    name = "我们的团队"

    more = True

    团队人员姓名 = models.CharField(max_length=255)
    团队人员职位 = models.CharField(max_length=255)


class OurPartners(BaseModel):


    name = "我们的合作伙伴"

    more = True
