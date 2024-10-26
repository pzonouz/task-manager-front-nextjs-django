
from rest_framework import viewsets

from categories.models import Category
from categories.serializers import CategorySerializer


class CategoryViewset(viewsets.ModelViewSet):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()
