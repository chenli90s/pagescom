from rest_framework import viewsets,permissions, authentication
from pages.model.about import *
from .serializers.about import *
from .permission import IsOwnerOrReadOnly
from rest_framework_jwt.authentication import JSONWebTokenAuthentication

class OurGuidanceViewSet(viewsets.ModelViewSet):

    queryset = OurGuidance.objects.all()
    serializer_class = OurGuidanceSerizlizers
    # permission_classes = (IsOwnerOrReadOnly,)
    authentication_classes = (JSONWebTokenAuthentication,)


class OurGoodViewSet(viewsets.ModelViewSet):

    queryset = OurGood.objects.all()
    serializer_class = OurGoodSerizlizers
    # permission_classes = (IsOwnerOrReadOnly,)
    authentication_classes = (JSONWebTokenAuthentication,)


class OurTeamViewSet(viewsets.ModelViewSet):

    queryset = OurTeam.objects.all()
    serializer_class = OurTeamSerizlizers
    # permission_classes = (IsOwnerOrReadOnly,)
    authentication_classes = (JSONWebTokenAuthentication,)

class OurPartnersViewSet(viewsets.ModelViewSet):

    queryset = OurPartners.objects.all()
    serializer_class = OurPartnersSerizlizers
    # permission_classes = (IsOwnerOrReadOnly,)
    authentication_classes = (JSONWebTokenAuthentication,)
