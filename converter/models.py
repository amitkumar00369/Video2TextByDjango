

# Create your models here.
# converter/models.py
from django.db import models

class VideoFile(models.Model):
    video = models.FileField(upload_to='download/')
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"Video {self.id} - {self.video.name}"
