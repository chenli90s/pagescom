from rest_framework import viewsets,permissions
from pages.model.contact import *
from .serializers.contact import *
from .permission import IsOwnerOrReadOnly
from rest_framework_jwt.authentication import JSONWebTokenAuthentication

class ContactsViewSet(viewsets.ModelViewSet):

    queryset = Contacts.objects.all()
    serializer_class = ContactsSerizlizers
    # permission_classes = (IsOwnerOrReadOnly,)
    authentication_classes = (JSONWebTokenAuthentication,)

class MapsViewSet(viewsets.ModelViewSet):

    queryset = Maps.objects.all()
    serializer_class = MapsSerizlizers
    # permission_classes = (IsOwnerOrReadOnly,)
    authentication_classes = (JSONWebTokenAuthentication,)