from django.db import models


class Tire(models.Model):
    FRONT = 1
    REAR = 2
    axischoices = [
        (FRONT, 'Vorne'),
        (REAR, 'Hinten'),
    ]
    tiredimension =  models.CharField(max_length = 20,blank=False)
    axis = models.IntegerField(choices=axischoices)

    def __str__(self):
        return f"Tire: {self.tiredimension} for {self.axis} axis"
