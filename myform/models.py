from django.db import models

class Person(models.Model):
    NAME_CHOICES = [
        ('first', 'First'),
        ('second', 'Second'),
        ('third', 'Third'),
        ('lifetime', 'Lifetime'),
    ]

    name = models.CharField(max_length=100)
    family_name = models.CharField(max_length=100)
    age = models.IntegerField()
    selection = models.CharField(max_length=10, choices=NAME_CHOICES)
    nationality = models.BooleanField(default=False)
    date_of_birth = models.DateField()  # Assuming you want to store the date in Gregorian format

    def __str__(self):
        return f"{self.name} {self.family_name}"
