import streamlit as st
import torch
import torchaudio
import os

# Import the necessary functions and classes
from System import TextTransform
from System  import SpeechRecognitionModel, load_model, speech_to_text

# Set page title
st.set_page_config(page_title="Speech Recognition App")

# Title
st.title("Speech Recognition App")

# Upload audio file
audio_file = st.file_uploader("Upload an audio file")

# Function to load the saved model
def load_model(model_path):
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    model = SpeechRecognitionModel(n_cnn_layers=3, n_rnn_layers=5, rnn_dim=512, n_class=29, n_feats=128)
    model.load_state_dict(torch.load(model_path, map_location=device))
    model.eval()
    return model, device

# Load resources
@st.cache_resource
def load_resources():
    model_path = "speech_recognition_model.pth"
    loaded_model, device = load_model(model_path)
    text_transform = TextTransform()
    valid_audio_transforms = torchaudio.transforms.MelSpectrogram()
    return loaded_model, device, text_transform, valid_audio_transforms

# Perform speech-to-text conversion
if audio_file is not None:
    # Check if the file is an audio file
    if audio_file.type.startswith('audio/'):
        loaded_model, device, text_transform, valid_audio_transforms = load_resources()
        audio_path = os.path.join("./", audio_file.name)
        with open(audio_path, "wb") as f:
            f.write(audio_file.getbuffer())

        # Play the audio file
        st.audio(audio_path, format='audio/wav')

        # Convert button
        if st.button("Convert to Text"):
            predicted_text = speech_to_text(audio_path, loaded_model, device, text_transform, valid_audio_transforms)
            st.success(f"Predicted Text: {predicted_text}")
    else:
        st.error("Please upload an audio file.")
else:
    st.info("Please upload an audio file to perform speech recognition.")
