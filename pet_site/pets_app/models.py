from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models


class Pet(models.Model):
    nickname = models.CharField(max_length=24, blank=True, null=False)
    age = models.PositiveIntegerField(null=False, blank=True, validators=[MinValueValidator(1), MaxValueValidator(40)])
    arriving_date = models.DateField(null=False)
    weight = models.DecimalField(max_digits=3, decimal_places=1, validators=[MinValueValidator(0.3), MaxValueValidator(80)])
    height = models.DecimalField(max_digits=4, decimal_places=2, validators=[MinValueValidator(10), MaxValueValidator(200)])
    special_signs = models.CharField(max_length=100, blank=True, null=False)
    archived = models.BooleanField(default=False)
