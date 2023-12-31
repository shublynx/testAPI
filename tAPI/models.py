from django.db import models

# Create your models here.
class Product(models.Model):

    def __str__(self):
        return self.title

    title = models.CharField(max_length=250)
    content = models.TextField()
    price = models.DecimalField(max_digits=15,decimal_places=2,default=99.99)