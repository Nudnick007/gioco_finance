from django.db import models

# Create your models here.
class Expenses(models.Model):
    Category = models.CharField(max_length=500)