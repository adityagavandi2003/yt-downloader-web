from django.db import models
from django.utils import timezone

class DownloadHistory(models.Model):
    title = models.CharField(max_length=255)
    url = models.URLField()
    format = models.CharField(max_length=10)
    quality = models.CharField(max_length=20)
    file_path = models.CharField(max_length=255)
    duration = models.IntegerField(default=0)
    is_playlist = models.BooleanField(default=False)
    playlist_title = models.CharField(max_length=255, null=True, blank=True)
    date = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ['-date']

    def __str__(self):
        return self.title
