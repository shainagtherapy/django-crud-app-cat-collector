from django.db import models
from django.urls import reverse

MEALS = (
    ('B', 'Breakfast'),
    ('L', 'Lunch'),
    ('D', 'Dinner')
)

class Toy(models.Model):
    name = models.CharField(max_length=50)
    color = models.CharField(max_length=20)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('toy-detail', kwargs={'pk_id': self.id})

class Cat(models.Model):
    name = models.CharField(max_length=100)
    breed = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    age = models.IntegerField()
    toys = models.ManyToManyField(Toy)

    # new code below
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('cat-detail', kwargs={'cat_id': self.id})
    
class Feeding(models.Model):
    date = models.DateField('Feeding Date')
    meal = models.CharField(max_length=1, choices=MEALS, default=MEALS[0][0])

    cat = models.ForeignKey(Cat, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.get_meal_display()} on {self.date}"
    
    # Define the default order of feedings
    class Meta:
        ordering = ['-date']  # This line makes the newest feedings appear first, no dash orders in oldest-newest
