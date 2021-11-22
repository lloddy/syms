from django.db import models
from django.urls import reverse
from datetime import date

# Create your models here.

MEALS = (
    ('B', 'Breakfast'),
    ('L', 'Lunch'),
    ('D', 'Dinner'),
)

class Affliction(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(max_length=250)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('afflictions_detail', kwargs={'pk': self.id})

class Sym(models.Model):
    name = models.CharField(max_length=100)
    gender = models.CharField(max_length=10)
    age = models.IntegerField()
    occupation = models.TextField(max_length=250)
    description = models.TextField(max_length=250)
    afflictions = models.ManyToManyField(Affliction)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('detail', kwargs={'sym_id': self.id})

    def fed_for_today(self):
        return self.feeding_set.filter(date=date.today()).count() >= len(MEALS)


class Feeding(models.Model):
    date = models.DateField('Feeding Date')
    meal = models.CharField(
        max_length=1,
        choices=MEALS,
        default=MEALS[0][0])
    
    sym = models.ForeignKey(Sym, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.get_meal_display()} on {self.date}'

    class Meta:
        ordering = ['-date']

class Photo(models.Model):
     url = models.CharField(max_length=200)
     sym = models.ForeignKey(Sym, on_delete=models.CASCADE)

     def __str__(self):
         return f'Photo for the sym_id: {self.sym_id} @{self.url}'