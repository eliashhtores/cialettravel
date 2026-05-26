from django.contrib import admin
from django.urls import include, path
from rest_framework.routers import DefaultRouter

from trips.views import DestinationViewSet, TripPackageViewSet, home

router = DefaultRouter()
router.register("destinations", DestinationViewSet)
router.register("packages", TripPackageViewSet)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include(router.urls)),
    path("", home, name="home"),
]
