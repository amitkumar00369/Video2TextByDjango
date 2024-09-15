# converter/views.py
from django.shortcuts import render, redirect

from googletrans import Translator
from rest_framework.views import APIView

from pydub import AudioSegment
import speech_recognition as sr
from rest_framework import status
import os

from rest_framework.response import Response
from .models import VideoFile  # Make sure to import your VideoFile model
from .serializers import VideoFileSerializer  # Import your serializer

class UploadVideo(APIView):
    def post(self, request):
        try:
            video = request.FILES.get('video')
            if not video:
                return Response({"message": "Video field is required."}, status=400)
            
            # Create the video object
            video_obj = VideoFile.objects.create(video=video)
            
            # Serialize the video object
            serializer = VideoFileSerializer(video_obj)
            
            return Response({"message": "Ok.", "data": serializer.data}, status=200)
        except Exception as e:
            return Response({"message": str(e)}, status=500)





def transcribe_audio_chunks(audio_path, chunk_duration=5):  # Reduce chunk duration to 10 seconds
    recognizer = sr.Recognizer()
    full_text = ""

    try:
        # Load the audio file using pydub
        audio = AudioSegment.from_wav(audio_path)
        audio_length = len(audio) / 1000  # Convert milliseconds to seconds

        for start_time in range(0, int(audio_length), chunk_duration):
            start_ms = start_time * 1000
            end_ms = min((start_time + chunk_duration) * 1000, len(audio))
            chunk = audio[start_ms:end_ms]

            # Save the chunk to a temporary file
            chunk_path = "temp_chunk.wav"
            chunk.export(chunk_path, format="wav")

            try:
                with sr.AudioFile(chunk_path) as source:
                    audio_data = recognizer.record(source)
                    # Specify language code for Punjabi or the intended language
                    text = recognizer.recognize_google(audio_data, language="en")
                    full_text += text + " "
            except sr.UnknownValueError:
                print(f"Chunk starting at {start_time}s could not be understood.")
            except sr.RequestError as e:
                print(f"Google Speech Recognition request failed; {str(e)}")
                break  # Stop processing on failure

            finally:
                # Clean up temporary file
                if os.path.exists(chunk_path):
                    os.remove(chunk_path)

    except Exception as e:
        print(f"An error occurred: {e}")

    return full_text.strip()

class ConvertAudio(APIView):
    def get(self, request, id=None):
        try:
            if not id:
                return Response({"message": "Video ID is required."}, status=400)
            
            # Fetch the video object
            video_obj = VideoFile.objects.filter(id=id).first()
            if not video_obj:
                return Response({"message": "Video not found."}, status=404)

            # Get the file path of the video
            video_path = video_obj.video.path
            print(f"Video path: {video_path}")

            # Define the audio output path
            audio_path = f"{os.path.splitext(video_path)[0]}.wav"
            audio_path_converted = convert_audio_format(audio_path)

            # Ensure the output directory exists
            audio_directory = os.path.dirname(audio_path_converted)
            os.makedirs(audio_directory, exist_ok=True)

            # Extract audio from video using ffmpeg
            ffmpeg_command = f'ffmpeg -i "{video_path}" -vn "{audio_path}"'
            ffmpeg_result = os.system(ffmpeg_command)
            if ffmpeg_result != 0:
                return Response({"message": "Failed to extract audio from video using ffmpeg."}, status=500)
            print(f"Audio extracted to: {audio_path}")

            # Check if audio file is empty
            if not os.path.exists(audio_path_converted) or os.path.getsize(audio_path_converted) == 0:
                return Response({"message": "Failed to extract or convert audio from video."}, status=500)

            # Convert audio to text using chunks
            text = transcribe_audio_chunks(audio_path_converted)
            
            # Translate text to multiple languages
            translator = Translator()
            languages = ['es', 'fr', 'de', 'hi','en']
            translations = {lang: translator.translate(text, dest=lang).text for lang in languages}

            context = {
                'text': text,
                'translations': translations,
            }

            return Response({"message": "Ok", "data": context}, status=200)
        except Exception as e:
            return Response({"message": str(e)}, status=500)

def convert_audio_format(audio_path):
    """Convert audio file to WAV format with standard settings."""
    output_path = f"{os.path.splitext(audio_path)[0]}_converted.wav"
    ffmpeg_command = f'ffmpeg -i "{audio_path}" -ar 16000 -ac 1 -f wav "{output_path}"'
    os.system(ffmpeg_command)
    return output_path
class getAll(APIView):
    def get(self,request):
        data=VideoFile.objects.all()
        sr=VideoFileSerializer(data,many=True)
      
        return Response({"message":"OK.","data":sr.data},200)
       
        