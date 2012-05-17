from django.db import models
from django.contrib.auth.models import User


class Result(models.Model):
    user = models.ForeignKey(User)
    expression = models.CharField(max_length=100)
    result = models.TextField()
