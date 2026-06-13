from django.shortcuts import render
from django.db.models import Sum
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from projects.models import Project
from lcca.models import LifecycleCost
from cppm.models import PortfolioAnalysis


class DashboardView(APIView):

    permission_classes = [IsAuthenticated]

    def get(self, request):

        total_projects = Project.objects.count()

        active_projects = Project.objects.filter(
            status='active'
        ).count()

        completed_projects = Project.objects.filter(
            status='completed'
        ).count()

        total_budget = Project.objects.aggregate(
            total=Sum('budget')
        )['total'] or 0

        total_lifecycle_cost = LifecycleCost.objects.aggregate(
            total=Sum('total_lifecycle_cost')
        )['total'] or 0

        top_project = PortfolioAnalysis.objects.order_by(
            '-priority_score'
        ).first()
        recent_projects = Project.objects.order_by(
            '-created_at'
        )[:5]

        recent_data = [
            {
                "id": p.id,
                "title": p.title,
                "status": p.status,
                "budget": p.budget
            }
            for p in recent_projects
        ]

        return Response({
            "total_projects": total_projects,
            "active_projects": active_projects,
            "completed_projects": completed_projects,
            "total_budget": total_budget,
            "total_lifecycle_cost": total_lifecycle_cost,
            "top_project": (
                top_project.project.title
                if top_project else None
            )
            ,"recent_projects": recent_data
        })
