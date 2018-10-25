from rest_framework import viewsets
from pages.model.home import *
from .serializers.home import *

class SliderViewSet(viewsets.ModelViewSet):

    queryset = Slider.objects.all()
    serializer_class = SliderSerizlizers
