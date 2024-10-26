from rest_framework import viewsets

from projects.models import Project
from projects.serializers import ProjectSerializer


class ProjectsViewset(viewsets.ModelViewSet):
    serializer_class = ProjectSerializer
    queryset = Project.objects.all()
