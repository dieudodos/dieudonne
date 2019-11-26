from django.db import models
from django.urls import reverse

# Create your models here.
class product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    description = models.TextField(max_length=3000)

    def __str__(self):
        return self.name
    def get_absolute_url(self):
        
        return reverse('product-detail', kwargs={'pk': self.pk})   

