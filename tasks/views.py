from rest_framework.viewsets import ModelViewSet

from tasks.models import Task
from tasks.serializers import TaskSerializer


class TasksViewset(ModelViewSet):
    queryset = Task.objects.all()
    serializer_class=TaskSerializer
