from django.db import models


class Country(models.Model):
    name = models.CharField(max_length=30)
    borders = models.ManyToManyField("self")
    dist = models.IntegerField(null=True)

    def __str__(self):
        """String for representing the Country object."""
        return self.name

