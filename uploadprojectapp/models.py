from django.db import models
import uuid

# Create your models here.
class Project(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=100)
    description = models.TextField()
    file = models.FileField(upload_to='project_files/')
    created_at = models.DateTimeField(auto_now_add=True)