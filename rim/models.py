from django.db import models

class Rim(models.Model):
    rimdimenesion = models.CharField(max_length = 20,blank=False,unique =True)
    def __str__(self):
        return f"Rim: {self.rimdimenesion}"
