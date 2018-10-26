from rest_framework import serializers
from pages.models import *

# base_fields = ('id', '是否展示', '上传图片', 'name', 'more')

class GlobalSerizlizers(serializers.ModelSerializer):

    class Meta:

        model = GlobalModel
        fields = ('logo',
                  '标题',
                  '地址',
                  '邮箱',
                  '电话',
                  '手机',
                  '关于我们',
                  '微信',
                  '微博',
                  'QQ',
                  '淘宝',
                  )