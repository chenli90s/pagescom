from rest_framework import serializers
from pages.model.contact import *

base_fields = ('id', '是否展示', 'name', 'more')

class ContactsSerizlizers(serializers.ModelSerializer):

    class Meta:

        model = Contacts
        fields = ('公司地址', '电话号码', '电子邮件', '信息描述')+base_fields

class MapsSerizlizers(serializers.ModelSerializer):

    class Meta:
        model = Maps
        fields = ('分享链接', ) + base_fields



