from django.db import models

# Create your models here.
class Produit(models.Model):
    ingredient = models.CharField(max_length=255)
    created_at = models.DateTimeField('created_at')