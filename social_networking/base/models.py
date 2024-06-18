from django.db import models
from base.choices import (
    STATE_CHOICES,
    StateStatuses
)
import uuid


class BaseTimeModel(models.Model):
    class Meta:
        abstract = True

    created_at = models.DateTimeField(
        auto_now_add=True, db_index=True)
    updated_at = models.DateTimeField(auto_now=True)


class BaseUUIDModel(models.Model):
    class Meta:
        abstract = True

    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)


class DeletionModel(models.Model):
    class Meta:
        abstract = True

    state = models.IntegerField(choices=STATE_CHOICES, default=StateStatuses.ACTIVE, db_index=True)


class AbstractBaseModel(BaseTimeModel, DeletionModel, BaseUUIDModel):
    class Meta:
        abstract = True
        ordering = ("-created_at",)

    def __str__(self):
        return str(self.uuid)