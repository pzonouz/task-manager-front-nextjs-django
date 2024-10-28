from rest_framework import viewsets

from categories.models import Category
from categories.serializers import CategorySerializer
from utils.permissions import IsAdminOrReadOnly


class CategoryViewset(viewsets.ModelViewSet):
    permission_classes = [IsAdminOrReadOnly]
    serializer_class = CategorySerializer
    queryset = Category.objects.all()
