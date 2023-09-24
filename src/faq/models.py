from django.db import models
from django.conf import settings
from django.utils import timezone


class Question(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.TextField()
    answer = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    resolved_date = models.DateTimeField(blank=True, null=True)

    def resolve(self):
        self.resolved_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
