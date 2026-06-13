from django.db import models
from projects.models import Project
from users.models import User


class Report(models.Model):

    REPORT_TYPES = (
        ('lcca', 'LCCA'),
        ('cppm', 'CPPM'),
        ('project', 'Project'),
    )

    project = models.ForeignKey(
        Project,
        on_delete=models.CASCADE
    )

    report_type = models.CharField(
        max_length=20,
        choices=REPORT_TYPES
    )

    generated_by = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return f"{self.project.title} - {self.report_type}"
