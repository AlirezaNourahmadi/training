from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class User(AbstractUser):
    ROLE_CHOISES = (
        ("student", "Student"),
        ("teacher", "Teacher"),
    )
    role = models.CharField(max_length=20, choices=ROLE_CHOISES, default="student")
    
    def __str__(self):
        return f"{self.username} ({self.role})"