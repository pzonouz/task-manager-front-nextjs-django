from rest_framework import viewsets

from priorities.models import Priority
from priorities.serializers import PrioritySerializer


class PriorityViewset(viewsets.ModelViewSet):
    serializer_class = PrioritySerializer
    queryset = Priority.objects.all()
