from django.contrib.auth.models import User
from django.db import models


class Requests(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '{}'.format(str(self.content))


class Reply(models.Model):
    message = models.ForeignKey(Requests, on_delete=models.CASCADE, null=True)
    content = models.TextField(null=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '{}'.format(str(self.message))

