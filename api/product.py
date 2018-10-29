from rest_framework import viewsets,permissions
from pages.model.product import *
from .serializers.product import *
from .permission import IsOwnerOrReadOnly

class OurProductViewSet(viewsets.ModelViewSet):

    queryset = OurProduct.objects.all()
    serializer_class = OurProductSerizlizers
    permission_classes = (IsOwnerOrReadOnly, )


class OurProductCateViewSet(viewsets.ModelViewSet):


    queryset = OurProductCate.objects.all()
    serializer_class = OurProductCateSerizlizers
    permission_classes = (IsOwnerOrReadOnly, )