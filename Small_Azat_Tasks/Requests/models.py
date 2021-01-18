from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone


class Requests(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    content = models.TextField()
    wrote_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return '{}'.format(str(self.content))


class Reply(models.Model):

    message = models.ForeignKey(Requests, on_delete=models.CASCADE, null=True)
    content = models.TextField(null=True)
    wrote_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return '{}'.format(str(self.message))

