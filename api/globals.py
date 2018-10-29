from rest_framework import viewsets,permissions,authentication
from pages.models import *
from .serializers.globals import *
from .permission import IsOwnerOrReadOnly

class GlobalsViewSet(viewsets.ModelViewSet):

    queryset = GlobalModel.objects.all()
    serializer_class = GlobalSerizlizers
    permission_classes = ( IsOwnerOrReadOnly, )



