from rest_framework import serializers
from pages.model.home import *

base_fields = ('id', 'ishow', 'image', )

class SliderSerizlizers(serializers.ModelSerializer):

    class Meta:

        model = Slider
        fields = ('口号', '响亮口号', '使命')+base_fields

class OurServiceSerizlizers(serializers.ModelSerializer):

    class Meta:

        model = Slider
        fields = ('口号', '服务类型', '服务描述')+base_fields



