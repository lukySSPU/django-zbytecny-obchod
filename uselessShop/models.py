from django.db import models

class Comment(models.Model):
    username = models.CharField(max_length=30, default="anonymous")
    text = models.TextField(default="...", blank=True)

class Item(models.Model):
    img = models.ImageField(upload_to="images/", default=None, blank=True)
    name = models.CharField(max_length=30)
    desc = models.TextField()
    price = models.FloatField()
    comment = models.ManyToManyField(Comment, blank=True, null=True)

    def __str__(self):
        return f"{self.name}"
