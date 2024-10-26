from django.db import models
from utils.models import TimeStampedModel


class Tag(TimeStampedModel):
    models.CharField(max_length=255)
