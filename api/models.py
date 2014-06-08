from django.db import models
from django.contrib.auth.models import User


class ApiToken(models.Model):
    user = models.ForeignKey(User)
    keyId = models.IntegerField()
    verificationCode = models.CharField(max_length=64)
