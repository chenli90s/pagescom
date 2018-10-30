from rest_framework import viewsets,permissions,authentication
from pages.models import *
from .serializers.globals import *
from .permission import IsOwnerOrReadOnly
from rest_framework_jwt.authentication import JSONWebTokenAuthentication


class GlobalsViewSet(viewsets.ModelViewSet):

    __doc__ = GlobalModel.name
    queryset = GlobalModel.objects.all()
    serializer_class = GlobalSerizlizers
    # permission_classes = ( IsOwnerOrReadOnly, )
    authentication_classes = (JSONWebTokenAuthentication,)


