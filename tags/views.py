from rest_framework import viewsets

from tags.models import Tag
from tags.serializers import TagSerializer


class TagsViewset(viewsets.ModelViewSet):
    serializer_class = TagSerializer
    queryset = Tag.objects.all()
