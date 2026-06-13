from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import Report
from .serializers import ReportSerializer


class ReportViewSet(viewsets.ModelViewSet):

    queryset = Report.objects.all()
    serializer_class = ReportSerializer
    permission_classes = [IsAuthenticated]
    @action(detail=True, methods=['get'])
    def project_summary(self, request, pk=None):
        report = self.get_object()
        project = report.project

        return Response({
            "project": project.title,
            "budget": project.budget,
            "status": project.status,
            "start_date": project.start_date,
            "end_date": project.end_date
        })