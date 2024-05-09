from django.db import models

class Item(models.Model):
    img = models.ImageField(upload_to="images/", default=None, blank=True)
    name = models.CharField(max_length=30)
    desc = models.TextField()
    price = models.FloatField()

    def __str__(self):
        return f"{self.name}"