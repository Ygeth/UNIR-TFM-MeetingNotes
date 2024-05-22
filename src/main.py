import models

model_whisper = models.load_whisper()

def transcript_whisper(audio_path):
    transcript = model_whisper.transcribe(audio_path)
    return transcript
  
  
# transcript_whisper("data/Refinamiento_AQ_audio.mp3")