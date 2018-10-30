from rest_framework import serializers
from pages.model.about import *

base_fields = ('id', '是否展示', '上传图片', 'name', 'more')

class OurGuidanceSerizlizers(serializers.ModelSerializer):

    class Meta:

        model = OurGuidance
        fields = ('业务类型', '业务描述')+base_fields



class OurGoodSerizlizers(serializers.ModelSerializer):

    class Meta:

        model = OurGood
        fields = ('擅长的领域描述', '擅长的领域分类')+base_fields

class OurTeamSerizlizers(serializers.ModelSerializer):

    class Meta:

        model = OurTeam
        fields = ('团队人员姓名', '团队人员职位')+base_fields

class OurPartnersSerizlizers(serializers.ModelSerializer):

    class Meta:

        model = OurGuidance
        fields = base_fields

