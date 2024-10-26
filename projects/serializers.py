from rest_framework import serializers

from projects.models import Project


class ProjectSerializer(serializers.Serializer):
    class Meta:
        model = Project
        fields = '__all__'
    
