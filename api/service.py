from rest_framework import viewsets,permissions
from pages.model.service import *
from .serializers.service import *
from .permission import IsOwnerOrReadOnly

class OurGuidancesViewSet(viewsets.ModelViewSet):

    queryset = OurGuidances.objects.all()
    serializer_class = OurGuidancesSerizlizers
    permission_classes = (IsOwnerOrReadOnly, )


class OurAdvantageViewSet(viewsets.ModelViewSet):
    queryset = OurAdvantage.objects.all()
    serializer_class = OurAdvantageSerizlizers
    permission_classes = (IsOwnerOrReadOnly, )




