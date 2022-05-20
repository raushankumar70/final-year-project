from django.db import models

# Create your models here.
class Item(models.Model):
    name = models.CharField(max_length=200)
    img = models.ImageField(upload_to='items', default='', blank=True, null=True)

    def __str__(self):
        return "%s" % (self.name)