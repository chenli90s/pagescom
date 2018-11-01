from rest_framework import serializers
from pages.model.product import *

base_fields = ('id', '是否展示', '上传图片', 'name', 'more')

class OurProductSerizlizers(serializers.ModelSerializer):

    class Meta:

        model = OurProduct
        fields = ('产品名字', '产品描述', '产品分类')+base_fields


class OurProductCateSerizlizers(serializers.ModelSerializer):

    class Meta:

        model = OurProductCate
        fields = ('产品分类', 'name', 'more')