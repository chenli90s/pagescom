from rest_framework import viewsets,permissions
from pages.models import *
from .serializers.globals import *


class GlobalsViewSet(viewsets.ModelViewSet):

    queryset = GlobalModel.objects.all()
    serializer_class = GlobalSerizlizers
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)



