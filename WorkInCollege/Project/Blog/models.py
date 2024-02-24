from django.db import models
from django.utils import timezone

class Data(models.Model):

    class isDelated(models.TextChoices):
        DELETE = 'DEL', 'Delete'
        EXISTS = 'EXI', 'Exists'

    login = models.CharField(max_length=10)
    password = models.CharField(max_length=20)
    create = models.DateTimeField(default=timezone.now)
    isDelated = models.CharField(max_length=3, choices = isDelated.choices, default = isDelated.EXISTS) 
