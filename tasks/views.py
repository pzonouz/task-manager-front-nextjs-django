from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from tasks.models import Task
from tasks.serializers import TaskSerializer


class TasksViewset(ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = TaskSerializer

    def create(self, request, *args, **kwargs):
        request.data["owner"] = request.user.id
        request.data["title"] = request.data["title"].lower()
        request.data["description"] = request.data["description"].lower()
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(
            serializer.data, status=status.HTTP_201_CREATED, headers=headers
        )

    def get_queryset(self):
        queryset = Task.objects.filter(owner=self.request.user)
        return queryset
