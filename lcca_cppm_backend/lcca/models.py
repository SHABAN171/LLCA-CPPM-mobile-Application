from django.db import models
from projects.models import Project

class LifecycleCost(models.Model):

    project = models.ForeignKey(
        Project,
        on_delete=models.CASCADE,
        related_name='lifecycle_costs'
    )

    initial_cost = models.DecimalField(max_digits=15, decimal_places=2, default=0)
    maintenance_cost = models.DecimalField(max_digits=15, decimal_places=2, default=0)
    operation_cost = models.DecimalField(max_digits=15, decimal_places=2, default=0)
    replacement_cost = models.DecimalField(max_digits=15, decimal_places=2, default=0)
    disposal_cost = models.DecimalField(max_digits=15, decimal_places=2, default=0)

    total_lifecycle_cost = models.DecimalField(
        max_digits=15,
        decimal_places=2,
        default=0
    )

    discount_rate = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        default=5
    )

    npv = models.DecimalField(
        max_digits=15,
        decimal_places=2,
        default=0
    )

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"LCCA - {self.project.title}"
