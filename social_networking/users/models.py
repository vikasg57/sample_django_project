from django.contrib.auth.models import User
from django.db import models
from base.models import AbstractBaseModel


class UserProfile(AbstractBaseModel):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name='profile')
    mobile = models.CharField(
        max_length=20, unique=True, null=True, blank=True, db_index=True)
    name = models.CharField(
        max_length=200, null=False, blank=False, db_index=True)
    profile_url = models.URLField(max_length=2048, null=True, blank=True)
    is_mobile_verified = models.BooleanField(default=False)
    is_email_verified = models.BooleanField(default=False)
    is_verified = models.BooleanField(default=False)

    def __str__(self):
        return self.user.email

    @property
    def first_name(self):
        return self.user.first_name

    @property
    def email(self):
        return self.user.email

    @property
    def last_name(self):
        return self.user.last_name
