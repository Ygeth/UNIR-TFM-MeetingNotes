## Origen del codigo:
# Gladia: https://www.gladia.io/blog/build-a-speaker-identification-system-for-online-meetings
# Pyannote: One-speaker-segmentation-model-to-rule-them-all https://herve.niderb.fr/fastpages/2022/10/23/One-speaker-segmentation-model-to-rule-them-all
# Pyannote: Streaming-voice-activity-detection https://herve.niderb.fr/fastpages/2021/08/05/Streaming-voice-activity-detection-with-pyannote.html

import torch
import numpy as np
from pyannote.audio import Model, SWF
from pyannote.core.segment import SlidingWindow
class VoiceActivityDetection:
    
    def __init__(self):
        self.model = Model.from_pretrained("pyannote/segmentation")
        self.model.eval()
        
    def __call__(self, current_buffer: SWF) -> SWF:
        
        # we start by applying the model on the current buffer
        with torch.no_grad():
            waveform = current_buffer.data.T
            segmentation = self.model(waveform[np.newaxis]).numpy()[0]

        # temporal resolution of the output of the model
        resolution = self.model.introspection.frames
        
        # temporal shift to keep track of current buffer start time
        resolution = SlidingWindow(start=current_buffer.sliding_window.start, 
                                duration=resolution.duration, 
                                step=resolution.step)
            
        # pyannote/segmentation pretrained model actually does more than just voice activity detection
        # see https://huggingface.co/pyannote/segmentation for more details.     
        speech_probability = np.max(segmentation, axis=-1, keepdims=True)
        
        return SWF(speech_probability, resolution)
      
      
      
## Step 1: Loading the necessary models
# First, we need to load the models to help us identify and diarize speakers from audio files. This involves setting up a GPU or CPU, loading a speaker embedding extraction model, and a speaker diarization model.
import torch
import torchaudio
from speechbrain.inference.speaker import EncoderClassifier
from pyannote.audio import Pipeline
from scipy.spatial.distance import cdist
# Check if CUDA is available and set the device accordingly
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
# Load pre-trained model for speaker embedding extraction and move it to the device
# Note: You need to obtain an API key from Hugging Face to use this model.
classifier = EncoderClassifier.from_hparams(source="speechbrain/spkrec-ecapa-voxceleb", run_opts={"device": device})
classifier = classifier.to(device)
# Pre-trained model for speaker diarization
# Note: The speaker diarization model also requires an API key from Hugging Face.
diarization = Pipeline.from_pretrained("pyannote/speaker-diarization-3.1",
                                        use_auth_token="YOUR_HUGGING_FACE_API_KEY")

## Step 2: Extracting known speaker embeddings
# Before recognizing speakers in a new recording, we need to have a reference of known speaker embeddings. Here, we extract embeddings from the sample audio files of well-known speakers.
known_speakers = []
known_speaker_ids = []  # To keep track of speaker IDs
for speaker_id, speaker_file in enumerate(["/path/to/SteveJobs.wav", "/path/to/ElonMusk.wav", "/path/to/NelsonMandela.wav"]):
    waveform, sample_rate = torchaudio.load(speaker_file)
    waveform = waveform.to(device)
    embedding = classifier.encode_batch(waveform)
    known_speakers.append(embedding.squeeze(1).cpu().numpy())  # Squeeze and move to CPU
    # Assign labels to each known speaker for identification
    if speaker_id == 0:
        known_speaker_ids.append("Steve Jobs")
    elif speaker_id == 1:
        known_speaker_ids.append("Elon Musk")
    elif speaker_id == 2:
        known_speaker_ids.append("Nelson Mandela")
        
## Step 3: Diarization of the meeting recording
# Now that we have our known speaker embeddings, we proceed to diarize an actual meeting recording to identify when each speaker is talking.

# Load and diarize the meeting recording
segments = diarization("/path/to/meeting_audio.wav")
# Once you've run the diarization model on a different audio samples, the output is a color-coded graph that contains meeting segments corresponding to different speakers.

# Step 4: Speaker identification process
# In this crucial step, we identify speakers in each audio segment derived from the meeting recording. This process involves iterating over each diarized segment, extracting audio for that segment, and comparing it against our known speaker embeddings.
# Set a threshold for similarity scores to determine when a match is considered successful
threshold = 0.8

# Iterate through each segment identified in the diarization process
for segment, label, confidence in segments.itertracks(yield_label=True):
    start_time, end_time = segment.start, segment.end

    # Load the specific audio segment from the meeting recording
    waveform, sample_rate = torchaudio.load("/path/to/meeting_audio.wav", num_frames=int((end_time-start_time)*sample_rate), frame_offset=int(start_time*sample_rate))
    waveform = waveform.to(device)

    # Extract the speaker embedding from the audio segment
    embedding = classifier.encode_batch(waveform).squeeze(1).cpu().numpy()

    # Initialize variables to find the recognized speaker
    min_distance = float('inf')
    recognized_speaker_id = None

    # Compare the segment's embedding to each known speaker's embedding using cosine distance
    for i, speaker_embedding in enumerate(known_speakers):
        distances = cdist([embedding], [speaker_embedding], metric="cosine")
        min_distance_candidate = distances.min()
        if min_distance_candidate < min_distance:
            min_distance = min_distance_candidate
            recognized_speaker_id = known_speaker_ids[i]

    # Output the identified speaker and the time range they were speaking, if a match is found
    if min_distance < threshold:
        print(f"Speaker {recognized_speaker_id} speaks from {start_time}s to {end_time}s.")
    else:
        print(f"No matching speaker found for segment from {start_time}s to {end_time}s.")

