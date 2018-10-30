from rest_framework import viewsets,permissions
from pages.model.product import *
from .serializers.product import *
from .permission import IsOwnerOrReadOnly
from rest_framework_jwt.authentication import JSONWebTokenAuthentication


class OurProductViewSet(viewsets.ModelViewSet):

    queryset = OurProduct.objects.all()
    serializer_class = OurProductSerizlizers
    # permission_classes = (IsOwnerOrReadOnly, )
    authentication_classes = (JSONWebTokenAuthentication,)

class OurProductCateViewSet(viewsets.ModelViewSet):


    queryset = OurProductCate.objects.all()
    serializer_class = OurProductCateSerizlizers
    # permission_classes = (IsOwnerOrReadOnly, )
    authentication_classes = (JSONWebTokenAuthentication,)