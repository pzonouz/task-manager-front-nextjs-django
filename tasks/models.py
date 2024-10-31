from django.db import models
from django.db.models.fields import validators
from django.utils.timezone import now

from utils.models import TimeStampedModel

STATUS_CHOICES = [("PR", "PROCCESSING"), ("CM", "COMPLETED"), ("CA", "CANCELLED")]


class Task(TimeStampedModel):
    title = models.CharField(max_length=255, unique=True)
    description = models.TextField()
    completed = models.BooleanField(default=False)
    status = models.CharField(choices=STATUS_CHOICES, default="PR", max_length=2)
    percentage = models.IntegerField(
        default=0,
        validators=[validators.MinValueValidator(0), validators.MaxValueValidator(100)],
    )
    owner = models.ForeignKey(
        "users.User", on_delete=models.CASCADE, related_name="tasks"
    )
    category = models.ForeignKey(
        "categories.Category",
        on_delete=models.SET_NULL,
        null=True,
        related_name="tasks",
    )
    project = models.ForeignKey(
        "projects.Project", on_delete=models.SET_NULL, null=True, related_name="tasks"
    )
    priority = models.ForeignKey(
        "priorities.Priority",
        on_delete=models.SET_NULL,
        null=True,
        related_name="tasks",
    )
    tags = models.ManyToManyField("tags.Tag", related_name="tasks", blank=True)
    due_date = models.DateTimeField(db_default=now())
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
