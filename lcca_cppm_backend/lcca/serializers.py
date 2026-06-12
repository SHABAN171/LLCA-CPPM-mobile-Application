from rest_framework import serializers
from .models import LifecycleCost

class LifecycleCostSerializer(serializers.ModelSerializer):

    project_name = serializers.CharField(
        source='project.title',
        read_only=True
    )

    class Meta:
        model = LifecycleCost
        fields = '__all__'