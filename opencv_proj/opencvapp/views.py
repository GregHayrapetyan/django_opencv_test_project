from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import cv2
import numpy as np
from .utils import opencv_func
from .models import VideoModel
from .forms import UploadForm
import asyncio

@csrf_exempt
def upload_video(request):
    form = UploadForm()
    download = None
    video_path = None
    media_path = None
    if request.method == 'POST':
        form = UploadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            download = 'download here'
        else:
            message = 'video not valid'
            return render(request, 'upload_video.html', {'message' : message})
        video = VideoModel.objects.all().order_by('-id')[0]
        video_path = opencv_func(video.video.path)
        media_path = f'media/finished_videos/{video_path}'
    return render(request, 'upload_video.html', {'form' : form, 'download':download, 'video_path':media_path})
  
  