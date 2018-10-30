from rest_framework import viewsets, authentication
from pages.model.home import *
from .serializers.home import *
from .permission import IsOwnerOrReadOnly
from rest_framework_jwt.authentication import JSONWebTokenAuthentication


class SliderViewSet(viewsets.ModelViewSet):

    __doc__ = Slider.name

    queryset = Slider.objects.all()
    serializer_class = SliderSerizlizers
    # permission_classes = (IsOwnerOrReadOnly,)
    authentication_classes = (JSONWebTokenAuthentication,)
    # authentication_classes = (authentication.TokenAuthentication,)  # 认证策略属性


class OurServiceViewSet(viewsets.ModelViewSet):

    __doc__ = OurService.name

    queryset = OurService.objects.all()
    serializer_class = OurServiceSerizlizers
    # permission_classes = (IsOwnerOrReadOnly, )
    authentication_classes = (JSONWebTokenAuthentication,)


class ChoiceusViewSet(viewsets.ModelViewSet):

    __doc__ = Choiceus.name
    queryset = Choiceus.objects.all()
    serializer_class = ChoiceusSerizlizers
    # permission_classes = (IsOwnerOrReadOnly,)
    authentication_classes = (JSONWebTokenAuthentication,)


class NewsViewSet(viewsets.ModelViewSet):

    __doc__ = News.name

    queryset = News.objects.all()
    serializer_class = NewsSerizlizers
    # permission_classes = (IsOwnerOrReadOnly,)
    authentication_classes = (JSONWebTokenAuthentication,)


class CommentViewSet(viewsets.ModelViewSet):

    __doc__ = Comment.name

    queryset = Comment.objects.all()
    serializer_class = CommentSerizlizers
    # permission_classes = (IsOwnerOrReadOnly,)
    authentication_classes = (JSONWebTokenAuthentication,)


class ClientsViewSet(viewsets.ModelViewSet):

    __doc__ = Clients.name

    queryset = Clients.objects.all()
    serializer_class = ClientsSerizlizers
    # permission_classes = (IsOwnerOrReadOnly,)
    authentication_classes = (JSONWebTokenAuthentication,)
