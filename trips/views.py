from django.shortcuts import render
from rest_framework import viewsets

from .models import Destination, TripPackage
from .serializers import DestinationSerializer, TripPackageSerializer


class DestinationViewSet(viewsets.ModelViewSet):
    queryset = Destination.objects.all()
    serializer_class = DestinationSerializer


class TripPackageViewSet(viewsets.ModelViewSet):
    queryset = TripPackage.objects.select_related("destination").all()
    serializer_class = TripPackageSerializer


def home(request):
    return render(
        request,
        "home.html",
        {
            "destinations": Destination.objects.all()[:3],
            "packages": TripPackage.objects.select_related("destination").all()[:3],
        },
    )
