from utils.audio_processor import process_input
from core.transcriber import transcribe_all

source="youtube-video-link"

chunks = process_input(source)
transcriptions = transcribe_all(chunks)
print(transcriptions)
