from django.utils import timezone

from django.db import models


class BaseModel(models.Model):
    class Meta:
        abstract = True

    created_date_time = models.DateTimeField(default=timezone.now)
    updated_date_time = models.DateTimeField(default=timezone.now, editable=True)
