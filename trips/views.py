from rest_framework import viewsets, permissions

from .models import Destination, TripPackage
from .serializers import DestinationSerializer, TripPackageSerializer


class DestinationViewSet(viewsets.ModelViewSet):
    queryset = Destination.objects.all()
    serializer_class = DestinationSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class TripPackageViewSet(viewsets.ModelViewSet):
    queryset = TripPackage.objects.select_related("destination").all()
    serializer_class = TripPackageSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
