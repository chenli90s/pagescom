from rest_framework import viewsets,permissions
from pages.model.service import *
from .serializers.service import *
from .permission import IsOwnerOrReadOnly
from rest_framework_jwt.authentication import JSONWebTokenAuthentication


class OurGuidancesViewSet(viewsets.ModelViewSet):

    queryset = OurGuidances.objects.all()
    serializer_class = OurGuidancesSerizlizers
    # permission_classes = (IsOwnerOrReadOnly, )
    authentication_classes = (JSONWebTokenAuthentication,)


class OurAdvantageViewSet(viewsets.ModelViewSet):
    queryset = OurAdvantage.objects.all()
    serializer_class = OurAdvantageSerizlizers
    # permission_classes = (IsOwnerOrReadOnly, )
    authentication_classes = (JSONWebTokenAuthentication,)




