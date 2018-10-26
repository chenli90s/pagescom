from rest_framework import viewsets,permissions
from pages.model.service import *
from .serializers.service import *


class OurGuidancesViewSet(viewsets.ModelViewSet):

    queryset = OurGuidances.objects.all()
    serializer_class = OurGuidancesSerizlizers
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


class OurAdvantageViewSet(viewsets.ModelViewSet):
    queryset = OurAdvantage.objects.all()
    serializer_class = OurAdvantageSerizlizers
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)




