from rest_framework import viewsets,permissions
from pages.model.about import *
from .serializers.about import *


class OurGuidanceViewSet(viewsets.ModelViewSet):

    queryset = OurGuidance.objects.all()
    serializer_class = OurGuidanceSerizlizers
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

class OurGoodViewSet(viewsets.ModelViewSet):

    queryset = OurGood.objects.all()
    serializer_class = OurGoodSerizlizers
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


class OurTeamViewSet(viewsets.ModelViewSet):

    queryset = OurTeam.objects.all()
    serializer_class = OurTeamSerizlizers
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

class OurPartnersViewSet(viewsets.ModelViewSet):

    queryset = OurPartners.objects.all()
    serializer_class = OurPartnersSerizlizers
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

