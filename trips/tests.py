from django.test import TestCase
from rest_framework.test import APIClient

from .models import Destination, TripPackage


class TravelApiTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.destination = Destination.objects.create(
            name="Santorini",
            country="Greece",
            description="Aegean island with whitewashed villages.",
        )
        TripPackage.objects.create(
            title="Santorini Getaway",
            destination=self.destination,
            duration_days=5,
            price="1499.99",
            summary="Sunset cruises, beaches, and local cuisine.",
        )

    def test_destination_list_api(self):
        response = self.client.get("/api/destinations/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()[0]["name"], "Santorini")

    def test_package_list_api(self):
        response = self.client.get("/api/packages/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()[0]["title"], "Santorini Getaway")

    def test_unauthenticated_write_is_rejected(self):
        response = self.client.post(
            "/api/destinations/",
            {"name": "Hack", "country": "Exploit", "description": "..."},
            format="json",
        )
        self.assertEqual(response.status_code, 403)
