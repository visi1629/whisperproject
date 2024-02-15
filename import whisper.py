import whisper

import os
audio_path = r"C://Users//vince//audioproject//audio1.mp3"   
print(os.path.exists(audio_path))  # path check

# Load Whisper model
model = whisper.load_model("base")

# Updated path to audio file
audio_path = r"C://Users//vince//audioproject//audio1.mp3"  

# Transcribe audio
result = model.transcribe(audio_path)

# Print the transcription
print(result["text"])
