from django import forms
from .models import VideoModel

class UploadForm(forms.ModelForm):
    class Meta:
        model = VideoModel
        fields = ['video']