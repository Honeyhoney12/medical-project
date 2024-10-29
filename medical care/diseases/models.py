from django.db import models

class Disease(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    cure = models.TextField()
    medicine = models.TextField()
    

    def __str__(self):
        return self.name
