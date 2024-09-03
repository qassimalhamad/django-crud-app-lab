from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
BRANDS = (
    ('BELL', 'BELL'),
    ('Arai', 'Arai'),
    ('Shoei', 'Shoei'),
)

class Helmet(models.Model):
    driver = models.CharField(max_length=100)
    year = models.IntegerField()
    description = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.driver} ({self.year})"
    
    def get_absolute_url(self):
        return reverse('helmet-detail', kwargs={'helmet_id': self.id})

class Brand(models.Model):
    brand = models.CharField(
        max_length=10,
        choices=BRANDS,
        default=BRANDS[0][0]
    )
    helmet = models.ForeignKey(Helmet, on_delete=models.CASCADE, related_name='brands')

    def __str__(self):
        return f'{self.get_brand_display()} on {self.helmet.driver}'
