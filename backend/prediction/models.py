from django.db import models

# Create your models here.
class HouseImage(models.Model):
    image = models.ImageField(blank=False, null=False)
    def __str__(self):
        return self.image.name
