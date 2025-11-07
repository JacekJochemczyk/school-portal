from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    USER_TYPES = [
        ('student', 'Student'),
        ('school', 'School'),
    ]

    user_type = models.CharField(max_length=10, choices=USER_TYPES)
    is_approved = models.BooleanField(default=False)  # dla szkół - wymagana akceptacja

    def __str__(self):
        return f"{self.username} ({self.user_type})"
    
    