import os
import models
from utils.videoUtils import VideoUtils
model_whisper = models.load_whisper()

def transcript_whisper(audio_path):
    transcript = model_whisper.transcribe(audio_path)
    return transcript
  

def transcriptVideo(video_path):
    ## check if video_path.replace(".mp4", "_audio.mp3") exists
    audio_path = video_path.replace(".mp4", "_audio.mp3")
    if not os.path.exists(video_path.replace(".mp4", "_audio.mp3")):
        audio_path = VideoUtils.extract_audio_from_video(video_path, video_path.replace(".mp4", "_audio.mp3"))
    
    
    transcript = transcript_whisper(audio_path)
    return transcript


def main():
    video_path = "../data/ENDV_intro.mp4"  # replace with your video path
    transcript = transcriptVideo(video_path)
    print(transcript)

if __name__ == "__main__":
    main()