from django.contrib.auth.models import AbstractUser
from django.db import models
class CustomUser(AbstractUser):
    mobile = models.CharField(max_length=15,verbose_name="موبایل")

    class Meta:
        verbose_name = "مشاور"
        verbose_name_plural = verbose_name