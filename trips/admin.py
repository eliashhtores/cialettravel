from django.contrib import admin

from .models import Destination, TripPackage


@admin.register(Destination)
class DestinationAdmin(admin.ModelAdmin):
    list_display = ("name", "country")


@admin.register(TripPackage)
class TripPackageAdmin(admin.ModelAdmin):
    list_display = ("title", "destination", "duration_days", "price")
