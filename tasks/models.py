import uuid
from django.db import models
from account.models import User
from projects.models import Project


class Task(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=250)
    description = models.TextField(blank=True, null=True)
    project = models.ForeignKey(Project, related_name="tasks", on_delete=models.CASCADE)
    created_by = models.ForeignKey(User, related_name="tasks", on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)
    due_date = models.DateTimeField(blank=True, null=True)
    done = models.BooleanField(default=False)

    def __str__(self):
        return self.name
