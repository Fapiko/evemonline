from django.db import models
from django.contrib.auth.models import User


class ApiToken(models.Model):
    user = models.ForeignKey(User)
    keyId = models.IntegerField()
    verificationCode = models.CharField(max_length=64)

class APIKeyInfo(models.Model):
    apiToken = models.ForeignKey(ApiToken)
    accessMask = models.IntegerField()
    type = models.IntegerField()
    expires = models.DateTimeField()
