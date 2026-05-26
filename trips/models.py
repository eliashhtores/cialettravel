from django.db import models


class Destination(models.Model):
    name = models.CharField(max_length=120)
    country = models.CharField(max_length=120)
    description = models.TextField()

    class Meta:
        ordering = ["name"]

    def __str__(self) -> str:
        return f"{self.name}, {self.country}"


class TripPackage(models.Model):
    title = models.CharField(max_length=120)
    destination = models.ForeignKey(Destination, on_delete=models.CASCADE, related_name="packages")
    duration_days = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    summary = models.TextField()

    class Meta:
        ordering = ["title"]

    def __str__(self) -> str:
        return self.title
