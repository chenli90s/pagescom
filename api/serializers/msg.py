from rest_framework import serializers
from pages.model.msg import *


class PriceSerizlizers(serializers.ModelSerializer):

    class Meta:

        model = Price
        fields = ('称呼', '电子邮件', '地址', "咨询目的", '咨询产品', '联系电话', '已读', 'id')


class MessageSerizlizers(serializers.ModelSerializer):

    class Meta:

        model = Message
        fields = ('全名', '电子邮件', '网站', "你的消息", '已读', 'id')

