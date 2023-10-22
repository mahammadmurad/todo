from django.db import models

class Todo(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField()
    priority = models.IntegerField()
    created_at = models.DateTimeField(null=True)


