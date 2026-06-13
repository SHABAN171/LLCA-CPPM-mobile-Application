from django.db import models
from projects.models import Project


class PortfolioAnalysis(models.Model):

    project = models.OneToOneField(
        Project,
        on_delete=models.CASCADE,
        related_name='portfolio_analysis'
    )

    expected_return = models.DecimalField(
        max_digits=15,
        decimal_places=2
    )

    investment_cost = models.DecimalField(
        max_digits=15,
        decimal_places=2
    )

    roi = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=0
    )

    risk_score = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        default=0
    )

    priority_score = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        default=0
    )

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.project.title
    
    def save(self, *args, **kwargs):
        if self.investment_cost > 0:
            self.roi = (
                (self.expected_return - self.investment_cost)
                / self.investment_cost
            ) * 100

        self.priority_score = (
            float(self.roi) * 0.7
        ) + (
            float(self.risk_score) * 0.3
        )

        super().save(*args, **kwargs)
