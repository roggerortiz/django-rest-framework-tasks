from django.db import models


class Task(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    important = models.BooleanField(default=False)

    def __str__(self):
        return self.title
