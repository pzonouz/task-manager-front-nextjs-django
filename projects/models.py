from django.db import models
from utils.models import TimeStampedModel


class Project(TimeStampedModel):
    name=models.CharField(max_length=255)
