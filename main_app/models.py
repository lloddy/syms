from django.db import models

# Create your models here.
class Sym(models.Model):
    name = models.CharField(max_length=100)
    gender = models.CharField(max_length=10)
    age = models.IntegerField()
    occupation = models.TextField(max_length=250)
    description = models.TextField(max_length=250)

    def __str__(self):
        return self.name
