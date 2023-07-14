from django.db import models

# Create your models here.



SEX_CHOICES = (
    ('M', 'Male'),
    ('F', 'Female'),
)


PORT_CHOICES = (
    ('C', 'Cherbourg'),
    ('Q', 'Queenstown'),
    ('S', 'Southampton'),
)


class Passenger(models.Model):
    name = models.CharField(max_length=100, blank=True)
    sex = models.CharField(max_length=1, choices=SEX_CHOICES)
    survived = models.BooleanField(default=True)
    age = models.FloatField(null=True)
    p_class = models.CharField(max_length=10)
    fare = models.FloatField(null=True)
    embarked = models.CharField(max_length=1, choices=PORT_CHOICES)

    def __str__(self):
        return self.name
