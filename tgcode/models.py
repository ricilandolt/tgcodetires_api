from django.db import models
from tire.models import Tire
from rim.models import Rim

class TgCode(models.Model):
    tgcode = models.CharField(max_length = 20, blank=False)
    tires = models.ManyToManyField(to=Tire)
    rims = models.ManyToManyField(to=Rim)
    def __str__(self):
        return f"TgCode: {self.tgcode} "