from django.db import models
from users.models import User

class Project(models.Model):

    STATUS_CHOICES = (
        ('pending', 'Pending'),
        ('active', 'Active'),
        ('completed', 'Completed'),
        ('delayed', 'Delayed'),
        ('cancelled', 'Cancelled'),
    )

    title = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)

    budget = models.DecimalField(max_digits=15, decimal_places=2)

    start_date = models.DateField()
    end_date = models.DateField()

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='pending'
    )

    manager = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        related_name="projects"
    )

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
