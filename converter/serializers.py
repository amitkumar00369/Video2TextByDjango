from rest_framework import serializers
from .models import VideoFile  # Make sure to import your VideoFile model

class VideoFileSerializer(serializers.ModelSerializer):
    class Meta:
        model = VideoFile
        fields = '__all__'
