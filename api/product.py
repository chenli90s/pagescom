from rest_framework import viewsets,permissions
from pages.model.product import *
from .serializers.product import *


class OurProductViewSet(viewsets.ModelViewSet):

    queryset = OurProduct.objects.all()
    serializer_class = OurProductSerizlizers
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


class OurProductCateViewSet(viewsets.ModelViewSet):


    queryset = OurProductCate.objects.all()
    serializer_class = OurProductCateSerizlizers
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)