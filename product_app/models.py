from django.db import models
from django.db.models.fields.related import create_many_to_many_intermediary_model

# Create your models here.
class Products_tabel(models.Model):
    name =  models.CharField(max_length=40)
    weight = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name