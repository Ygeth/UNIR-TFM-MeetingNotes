from moviepy.audio.io.AudioFileClip import AudioFileClip


def extract_audio_from_video(video_path, audio_path):# -> Any:
    from moviepy.editor import VideoFileClip
    # Load the video clip
    clip = VideoFileClip(video_path)
    # Extract the audio from the video clip
    # clip.audio
    audio_clip: AudioFileClip | None = clip.audio
    # # Save the audio clip as WAV file
    audio_clip.write_audiofile(audio_path)
    
    return audio_path
  
# extract_audio_from_video("data/refinamiento_AQ.mp4", "data/refinamiento_AQ_audio.mp3")