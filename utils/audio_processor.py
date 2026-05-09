import os
import yt_dlp
from pydub import AudioSegment

DOWNLOAD_DIR = "downloads"
os.makedirs(DOWNLOAD_DIR, exist_ok=True)

def download_youtube_audio(url):
    output_path = os.path.join(DOWNLOAD_DIR, "%(title)s.%(ext)s")
    yt_opts = {
        'format': 'bestaudio/best',
        'outtmpl': output_path,
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'wav',
            'preferredquality': '192',
        }],
        "quiet": True,
    }

    with yt_dlp.YoutubeDL(yt_opts) as ydl:
        info = ydl.extract_info(url, download=True)
        filename = ydl.prepare_filename(info).replace(".webm", ".wav").replace(".m4a", ".wav")
    return filename

data = download_youtube_audio("youtube-video-link")

def convert_to_wav(input_path: str) -> str:
    """Convert any audio/video fil to WAV format using pydub."""
    output_path = os.path.splitext(input_path)[0] + "_conveted.wav"
    audio = AudioSegment.from_file(input_path)
    audio = audio.set_channels(1).set_frame_rate(16000) #mono & 16kHz
    audio.export(output_path, format="wav")
    return output_path

data = convert_to_wav(data)
print(data)