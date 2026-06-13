from rest_framework import serializers
from .models import Report


class ReportSerializer(serializers.ModelSerializer):

    project_name = serializers.CharField(
        source='project.title',
        read_only=True
    )

    class Meta:
        model = Report
        fields = '__all__'