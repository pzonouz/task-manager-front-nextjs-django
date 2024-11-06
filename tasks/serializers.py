from rest_framework import serializers

from categories.serializers import CategorySerializer
from tasks.models import Task


class TaskSerializer(serializers.ModelSerializer):
    category_full = CategorySerializer(source="category", read_only=True)
    priority_full = CategorySerializer(source="priority", read_only=True)

    class Meta:
        model = Task
        fields = [
            "id",
            "title",
            "description",
            "completed",
            "created_at",
            "updated_at",
            "owner",
            "category",
            "project",
            "priority",
            "tags",
            "due_date",
            "status",
            "percentage",
            "category_full",
            "priority_full",
        ]
