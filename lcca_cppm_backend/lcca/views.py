from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import LifecycleCost
from .serializers import LifecycleCostSerializer


class LifecycleCostViewSet(viewsets.ModelViewSet):

    queryset = LifecycleCost.objects.all()
    serializer_class = LifecycleCostSerializer
    permission_classes = [IsAuthenticated]

    @action(detail=True, methods=['get'])
    def summary(self, request, pk=None):

        record = self.get_object()

        return Response({
            "project": record.project.title,
            "total_cost": record.total_lifecycle_cost,
            "npv": record.npv,
            "discount_rate": record.discount_rate
        })