from rest_framework import viewsets,permissions, authentication
from pages.model.about import *
from .serializers.about import *
from .permission import IsOwnerOrReadOnly

class OurGuidanceViewSet(viewsets.ModelViewSet):

    queryset = OurGuidance.objects.all()
    serializer_class = OurGuidanceSerizlizers
    permission_classes = (IsOwnerOrReadOnly,)
    # authentication_classes = (authentication.TokenAuthentication,)


class OurGoodViewSet(viewsets.ModelViewSet):

    queryset = OurGood.objects.all()
    serializer_class = OurGoodSerizlizers
    permission_classes = (IsOwnerOrReadOnly,)
    # authentication_classes = (authentication.TokenAuthentication,)


class OurTeamViewSet(viewsets.ModelViewSet):

    queryset = OurTeam.objects.all()
    serializer_class = OurTeamSerizlizers
    permission_classes = (IsOwnerOrReadOnly,)
    # permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly)

class OurPartnersViewSet(viewsets.ModelViewSet):

    queryset = OurPartners.objects.all()
    serializer_class = OurPartnersSerizlizers
    permission_classes = (IsOwnerOrReadOnly,)
    # permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly)

