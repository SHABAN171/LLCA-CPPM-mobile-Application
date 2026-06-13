from rest_framework import serializers
from .models import PortfolioAnalysis


class PortfolioAnalysisSerializer(serializers.ModelSerializer):

    project_name = serializers.CharField(
        source='project.title',
        read_only=True
    )

    class Meta:
        model = PortfolioAnalysis
        fields = '__all__'