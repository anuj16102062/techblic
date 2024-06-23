from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    ADMIN = 'admin'
    SOLUTION_PROVIDER = 'solution_provider'
    SOLUTION_SEEKER = 'solution_seeker'

    ROLE_CHOICES = (
        (ADMIN, 'Admin'),
        (SOLUTION_PROVIDER, 'Solution Provider'),
        (SOLUTION_SEEKER, 'Solution Seeker'),
    )

    role = models.CharField(max_length=20, choices=ROLE_CHOICES)
    otp = models.CharField(max_length=16,default='')
