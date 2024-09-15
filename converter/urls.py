# converter/urls.py
from django.urls import path
from .views import UploadVideo, ConvertAudio,getAll

urlpatterns = [
    path('upload', UploadVideo.as_view(), name='upload_video'),
    path('convert/<int:id>/', ConvertAudio.as_view(), name='convert_audio'),
    path("allVideos",getAll.as_view())
]
