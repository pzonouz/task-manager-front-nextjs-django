from django.db import models
from django.utils.timezone import now
from utils.models import TimeStampedModel

STATUS_CHOICES = [
        ("PR","PROCCESSING"),
        ("CM","COMPLETED"),
        ("CA","CANCELLED")
]

class Task(TimeStampedModel):
    title = models.CharField(max_length=255)
    description = models.TextField()
    completed = models.BooleanField(default=False)
    status=models.CharField(choices=STATUS_CHOICES,default="PR",max_length=2)
    owner=models.ForeignKey("users.User", on_delete=models.CASCADE,related_name="tasks")
    category=models.ForeignKey("categories.Category", on_delete=models.CASCADE,related_name="tasks")
    project=models.ForeignKey("projects.Project", on_delete=models.CASCADE,related_name="tasks")
    tags=models.ManyToManyField("tags.Tag",related_name="tasks")
    due_date=models.DateTimeField(db_default=now())
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
