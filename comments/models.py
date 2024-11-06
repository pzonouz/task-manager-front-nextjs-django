from django.db import models


class Comment(models.Model):
    text = models.TextField()
    user = models.ForeignKey(
        "users.User", on_delete=models.CASCADE, related_name="comments"
    )
    task = models.ForeignKey(
        "tasks.Task", on_delete=models.CASCADE, related_name="comments"
    )
