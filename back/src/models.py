from pyannote.audio.core.pipeline import Pipeline
# from whisper.model import Whisper
import whisper
from pyannote.audio import Pipeline
from pyannote_whisper import utils

def load_whisper():
  # Probar NVIDIA: https://huggingface.co/nvidia/stt_es_conformer_transducer_large
  # https://huggingface.co/facebook/wav2vec2-large-es-voxpopuli
  # https://huggingface.co/jonatasgrosman/wav2vec2-large-xlsr-53-spanish --> 8,4% WER
  # https://huggingface.co/zuazo/whisper-medium --> 5.2% WEB
  # https://huggingface.co/zuazo/whisper-medium-es --> 

  model_whisper = whisper.load_model("medium")
  return model_whisper
