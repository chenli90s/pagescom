from rest_framework import serializers
from pages.model.service import *

base_fields = ('id', '是否展示', '上传图片', 'name', 'more')


class OurGuidancesSerizlizers(serializers.ModelSerializer):

    class Meta:

        model = OurGuidances
        fields = ('服务类型', '指导描述')+base_fields


class OurAdvantageSerizlizers(serializers.ModelSerializer):

    class Meta:

        model = OurAdvantage
        fields = ('优点描述', '优点分类')+base_fields


