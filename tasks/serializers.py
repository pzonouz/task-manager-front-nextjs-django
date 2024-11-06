from rest_framework import serializers

from categories.serializers import CategorySerializer
from comments.serializers import CommentSerializer
from priorities.serializers import PrioritySerializer
from tasks.models import Task


class TaskSerializer(serializers.ModelSerializer):
    category_full = CategorySerializer(source="category", read_only=True)
    priority_full = PrioritySerializer(source="priority", read_only=True)
    comments_full = CommentSerializer(source="comments", many=True, read_only=True)

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
            "comments_full",
        ]
