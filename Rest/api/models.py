from django.db import models

# Create your models here.




class Prezent(models.Model):
    name=models.CharField(max_length=100)
    price=models.DecimalField(max_digits=8, decimal_places=2)
    description=models.TextField()
    created=models.DateTimeField(auto_now_add=True)
