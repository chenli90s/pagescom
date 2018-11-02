from rest_framework import viewsets, authentication
from pages.model.msg import *
from .serializers.msg import *
from rest_framework_jwt.authentication import JSONWebTokenAuthentication

class PriceViewSet(viewsets.ModelViewSet):

    __doc__ = Price.name

    queryset = Price.objects.all()
    serializer_class = PriceSerizlizers
    authentication_classes = (JSONWebTokenAuthentication,)


class MessageViewSet(viewsets.ModelViewSet):

    __doc__ = Message.name

    queryset = Message.objects.all()
    serializer_class = MessageSerizlizers
    authentication_classes = (JSONWebTokenAuthentication,)
