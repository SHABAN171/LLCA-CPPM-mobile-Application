from django.db import models
from django.contrib.auth.models import AbstractUser

#model
class User(AbstractUser):

    ROLE_CHOICES = (
        ('admin', 'Admin'),
        ('manager', 'Project Manager'),
        ('analyst', 'Financial Analyst'),
        ('viewer', 'Viewer'),
    )

    role = models.CharField(
        max_length=50,
        choices=ROLE_CHOICES,
        default='viewer'
    )