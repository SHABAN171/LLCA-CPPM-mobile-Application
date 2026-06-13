from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from .models import PortfolioAnalysis
from .serializers import PortfolioAnalysisSerializer


class PortfolioAnalysisViewSet(viewsets.ModelViewSet):

    queryset = PortfolioAnalysis.objects.all()
    serializer_class = PortfolioAnalysisSerializer
    permission_classes = [IsAuthenticated]
