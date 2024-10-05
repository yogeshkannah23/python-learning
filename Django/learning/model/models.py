from django.db import models

# Create your models here.

class Person(models.Model):
    name = models.CharField(max_length=30,blank=False,default="summa")
    age = models.IntegerField(max_length=10)


class ShirtManager(models.Manager):
    def smallshirts(self):
        return super().get_queryset().filter(shirt_size='M')


class Shirt(models.Model):
    SHIRT_SIZES = [
        ("S", "Small"),
        ("M", "Medium"),
        ("L", "Large"),
    ]
    name = models.CharField(max_length=60)
    shirt_size = models.CharField(max_length=1, choices=SHIRT_SIZES)

    # objects = models.Manager()  # Default manager
    # small_shirts = ShirtManager()  # Custom manager