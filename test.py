from dotenv import load_dotenv

load_dotenv()  # MUST be before any core/ imports
from utils.audio_processor import process_input
from core.transcriber import transcribe_all
import os

print("KEY LOADED:", os.getenv("SARVAM_API_KEY"))  # should print your key
print("CWD", os.getcwd())

source = "https://www.youtube.com/watch?v=tplWXd_T7YQ"
language = "hinglish"  # change to "hinglish" to text sarvam

chunks = process_input(source)
transcriptions = transcribe_all(chunks, language=language)

print("\n=== TRANSCRIPT \ ===\n")
print(transcriptions)
