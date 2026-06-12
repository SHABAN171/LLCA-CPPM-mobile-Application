from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from .models import LifecycleCost
from .serializers import LifecycleCostSerializer

class LifecycleCostViewSet(viewsets.ModelViewSet):

    queryset = LifecycleCost.objects.all()
    serializer_class = LifecycleCostSerializer
    permission_classes = [IsAuthenticated]