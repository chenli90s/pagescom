from rest_framework import viewsets,permissions
from pages.model.product import *
from .serializers.product import *


class OurProductViewSet(viewsets.ModelViewSet):

    queryset = OurProduct.objects.all()
    serializer_class = OurProductSerizlizers
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)