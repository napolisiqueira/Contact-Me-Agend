from django.utils import timezone
from django.db import models

# Create your models here.

class Contact(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50, blank=True)
    phone = models.CharField(max_length=50)
    email = models.EmailField(max_length=50, blank=True)
    created_it = models.DateTimeField(default=timezone.now) 
    description = models.TextField(blank=True)
    category = models.CharField(max_length=50, blank=True)

    def __str__(self) -> str:
        return self.first_name