from django.db import models

class MenuItem(models.Model):
    CATEGORY_CHOICES = (
        ('entree', 'Entree'),
        ('app', 'Appetizer'),
    )
    
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    spice_level = models.IntegerField(default=0)
    category = models.CharField(max_length=10, choices=CATEGORY_CHOICES)
    
    def __str__(self):
        return f"{self.name} ({self.category}) - ${self.price}, Spice Level: {self.spice_level}"
