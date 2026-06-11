from rest_framework import serializers
from .models import Project

class ProjectSerializer(serializers.ModelSerializer):

    manager_name = serializers.CharField(
        source='manager.username',
        read_only=True
    )

    class Meta:
        model = Project
        fields = [
            'id',
            'title',
            'description',
            'budget',
            'start_date',
            'end_date',
            'status',
            'manager',
            'manager_name',
            'created_at'
        ]