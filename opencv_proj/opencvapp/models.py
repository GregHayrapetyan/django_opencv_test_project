from django.db import models

class VideoModel(models.Model):
    video = models.FileField(upload_to='videos/')