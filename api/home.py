from rest_framework import viewsets,permissions
from pages.model.home import *
from .serializers.home import *

class SliderViewSet(viewsets.ModelViewSet):

    queryset = Slider.objects.all()
    serializer_class = SliderSerizlizers
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


class OurServiceViewSet(viewsets.ModelViewSet):

    queryset = OurService.objects.all()
    serializer_class = OurServiceSerizlizers
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


class ChoiceusViewSet(viewsets.ModelViewSet):

    queryset = Choiceus.objects.all()
    serializer_class = ChoiceusSerizlizers
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

class NewsViewSet(viewsets.ModelViewSet):

    queryset = News.objects.all()
    serializer_class = NewsSerizlizers
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


class CommentViewSet(viewsets.ModelViewSet):

    queryset = Comment.objects.all()
    serializer_class = CommentSerizlizers
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

class ClientsViewSet(viewsets.ModelViewSet):

    queryset = Clients.objects.all()
    serializer_class = ClientsSerizlizers
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
