from rest_framework import viewsets,permissions
from pages.model.contact import *
from .serializers.contact import *


class ContactsViewSet(viewsets.ModelViewSet):

    queryset = Contacts.objects.all()
    serializer_class = ContactsSerizlizers
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)