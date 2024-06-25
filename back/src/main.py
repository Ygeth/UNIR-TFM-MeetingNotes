import os
import models
import gradio as gr

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
    # video_path = "../data/ENDV_intro.mp4"  # replace with your video path
    # transcript = transcriptVideo(video_path)
    print(transcript)
    
    
    ## Gradio Interface
    iface = gr.Interface(
        fn=rag_chain,
        inputs= ["text", "text"],
        outputs= "text",
        title = "Rag Chain Wikpedia Question Answering",
        description = "Introduce una Url de la wikipedia y una pregunta"
    )
    
    ## Añadir boton con url relativa y generate transcript
    ## Load transcript con los preguardados o subir uno nuevo(estructura Whisper).
    
    # Question about context
    # Question all
    # Task extraction
    # Summarize
            
    iface.launch()

if __name__ == "__main__":
    main()