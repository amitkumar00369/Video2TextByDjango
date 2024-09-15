

# Video2Text Django Project

This project allows users to upload video files, convert the audio to text, and translate the transcribed text into multiple languages.

## Features

- **Video Upload**: Users can upload video files, and the app saves them in the database.
- **Audio Transcription**: The audio from the video is extracted and transcribed into text.
- **Translation**: The transcribed text can be translated into multiple languages.
- **Retrieve All Videos**: Get a list of all uploaded videos.

## Technologies Used

- **Django**: A high-level Python web framework.
- **Django Rest Framework (DRF)**: For building API endpoints.
- **Googletrans**: For language translation.
- **pydub**: For audio processing and chunking.
- **SpeechRecognition**: For converting audio to text.
- **ffmpeg**: For audio extraction from video.

## Requirements

To run this project, you'll need to have the following dependencies installed. You can install them using the command:

```bash
pip install -r requirements.txt
```

### `requirements.txt`
```
asgiref==3.8.1
certifi==2024.8.30
chardet==3.0.4
charset-normalizer==3.3.2
Django==5.1.1
djangorestframework==3.15.2
googletrans==4.0.0rc1
h11==0.9.0
h2==3.2.0
hpack==3.0.0
hstspreload==2024.9.1
httpcore==0.9.1
httpx==0.13.3
hyperframe==5.2.0
idna==2.10
pydub==0.25.1
pytube==15.0.0
requests==2.32.3
rfc3986==1.5.0
sniffio==1.3.1
SpeechRecognition==3.10.4
sqlparse==0.5.1
typing_extensions==4.12.2
tzdata==2024.1
urllib3==2.2.2
```

## Project Setup

1. Clone the repository:

```bash
git clone https://github.com/amitkumar00369/Video2TextByDjango.git
cd Video2TextByDjango
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Run migrations to set up the database:

```bash
python manage.py migrate
```

4. Start the Django development server:

```bash
python manage.py runserver
```

5. Use a tool like Postman or curl to interact with the API.

## API Endpoints

### 1. Upload Video

- **Endpoint**: `/upload`
- **Method**: `POST`
- **Description**: Uploads a video file to the server.
- **Request**: `multipart/form-data`
  - `video`: The video file to upload.

#### Example Request (using curl):

```bash
curl -X POST -F "video=@path_to_your_video_file" http://localhost:8000/upload
```

### 2. Convert Video Audio to Text

- **Endpoint**: `/convert/<int:id>/`
- **Method**: `GET`
- **Description**: Converts the audio of the uploaded video (identified by `id`) to text, and translates the text into multiple languages.

#### Example Request (using curl):

```bash
curl -X GET http://localhost:8000/convert/1/
```

### 3. Get All Videos

- **Endpoint**: `/allVideos`
- **Method**: `GET`
- **Description**: Retrieves a list of all uploaded videos.

#### Example Request (using curl):

```bash
curl -X GET http://localhost:8000/allVideos
```

## Notes

- Ensure `ffmpeg` is installed on your system for audio extraction from video.
- The default chunk size for transcribing audio is set to 5 seconds to avoid long processing times.
  
### ffmpeg Installation
For most systems, you can install ffmpeg using:

- **Ubuntu/Debian**: `sudo apt-get install ffmpeg`
- **MacOS**: `brew install ffmpeg`
- **Windows**: Download from [here](https://ffmpeg.org/download.html)

## Future Improvements

- **Language Detection**: Automatically detect the language of the video/audio.
- **UI Interface**: Provide a user interface for easy video uploads and text translations.

## License

This project is open source and available under the [MIT License](https://opensource.org/licenses/MIT).

---
