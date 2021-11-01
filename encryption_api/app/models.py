from django.db import models

# Create your models here.

class Encoder(models.Model) :
    encoder_number = models.CharField(max_length=100)

