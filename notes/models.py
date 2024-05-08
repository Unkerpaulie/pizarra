import uuid
from django.db import models
from account.models import User
from projects.models import Project


class Note(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    project = models.ForeignKey(Project, related_name="notes", on_delete=models.CASCADE)
    title = models.CharField(max_length=250)
    body = models.TextField(blank=True, null=True)
    created_by = models.ForeignKey(User, related_name="notes", on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    