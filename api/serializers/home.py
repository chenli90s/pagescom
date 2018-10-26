from rest_framework import serializers
from pages.model.home import *

base_fields = ('id', '是否展示', '上传图片', 'name', 'more')

class SliderSerizlizers(serializers.ModelSerializer):

    class Meta:

        model = Slider
        fields = ('口号', '响亮口号', '使命')+base_fields

class OurServiceSerizlizers(serializers.ModelSerializer):

    class Meta:

        model = Slider
        fields = ('口号', '服务类型', '服务描述')+base_fields


class ChoiceusSerizlizers(serializers.ModelSerializer):

    class Meta:

        model = Slider
        fields = ('选择原因', '选择原因标题')+base_fields

class NewsSerizlizers(serializers.ModelSerializer):

    class Meta:

        model = Slider
        fields = ('消息内容', '消息标题')+base_fields


class CommentSerizlizers(serializers.ModelSerializer):

    class Meta:

        model = Slider
        fields = ('客户头像', '客户姓名', '客户职位', '客户描述')+base_fields


class ClientsSerizlizers(serializers.ModelSerializer):

    class Meta:
        model = Slider
        fields = base_fields


