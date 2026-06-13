from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import PortfolioAnalysis
from .serializers import PortfolioAnalysisSerializer


class PortfolioAnalysisViewSet(viewsets.ModelViewSet):

    queryset = PortfolioAnalysis.objects.all()
    serializer_class = PortfolioAnalysisSerializer
    permission_classes = [IsAuthenticated]
@action(detail=False, methods=['get'])
def rankings(self, request):

    projects = PortfolioAnalysis.objects.order_by(
        '-priority_score'
    )

    serializer = self.get_serializer(
        projects,
        many=True
    )

    return Response(serializer.data)