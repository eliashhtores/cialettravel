from rest_framework import serializers

from .models import Destination, TripPackage


class DestinationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Destination
        fields = ["id", "name", "country", "description"]


class TripPackageSerializer(serializers.ModelSerializer):
    destination_name = serializers.CharField(source="destination.name", read_only=True)

    class Meta:
        model = TripPackage
        fields = [
            "id",
            "title",
            "destination",
            "destination_name",
            "duration_days",
            "price",
            "summary",
        ]
