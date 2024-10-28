from rest_framework import viewsets

from priorities.models import Priority
from priorities.serializers import PrioritySerializer
from utils.permissions import IsAdminOrReadOnly


class PriorityViewset(viewsets.ModelViewSet):
    permission_classes = [IsAdminOrReadOnly]
    serializer_class = PrioritySerializer
    queryset = Priority.objects.all()
