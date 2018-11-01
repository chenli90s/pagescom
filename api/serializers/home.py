from rest_framework import serializers
from pages.model.home import *

base_fields = ('id', '是否展示', '上传图片', 'name', 'more')

class SliderSerizlizers(serializers.ModelSerializer):

    class Meta:

        model = Slider
        fields = ('口号', '响亮口号', '使命')+base_fields

class OurServiceSerizlizers(serializers.ModelSerializer):

    class Meta:

        model = OurService
        fields = ('服务类型', '服务描述')+base_fields


class ChoiceusSerizlizers(serializers.ModelSerializer):

    class Meta:

        model = Choiceus
        fields = ('选择原因', '选择原因标题', '图标')+base_fields

class NewsSerizlizers(serializers.ModelSerializer):

    class Meta:

        model = News
        fields = ('消息内容', '消息标题', '时间')+base_fields


class CommentSerizlizers(serializers.ModelSerializer):

    class Meta:

        model = Comment
        fields = ('上传图片', '客户姓名', '客户职位', '客户描述')+base_fields


class ClientsSerizlizers(serializers.ModelSerializer):

    class Meta:
        model = Clients
        fields = base_fields+('客户姓名',)


