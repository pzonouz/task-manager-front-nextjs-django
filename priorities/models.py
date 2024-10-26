from django.db import models
from utils.models import TimeStampedModel


class Priority(TimeStampedModel):
    name=models.CharField(max_length=255)
