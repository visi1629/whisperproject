import os
import whisper
from spleeter.separator import Separator

def main():
    #Path to  audio file
    audio_path = r"C://Users//vince//audioproject//audio3.mp3"
    output_path = r"C://Users//vince//audioproject//output"
    transcription_folder = os.path.join(output_path, "transcriptions")

    # Create a directory for transcriptions
    if not os.path.exists(transcription_folder):
        os.makedirs(transcription_folder)

    print(os.path.exists(audio_path))  # path check to ensure the file exists

    # Initialize Spleeter with the 2stems model (vocals and instrumental)
    separator = Separator('spleeter:2stems')

    # Process the file with Spleeter to separate the vocals
    separator.separate_to_file(audio_path, output_path)

    # Define the path to the separated vocal file
    vocals_path = os.path.join(output_path, 'audio3', 'vocals.wav')

    # Check if the vocals file was created successfully
    print(os.path.exists(vocals_path))

    # Load the Whisper model
    model = whisper.load_model("medium")

    # Transcribe the separated vocals
    result = model.transcribe(vocals_path)

    # Print the transcription
    print(result["text"])

    # Save the transcription to a file
    transcription_file_path = os.path.join(transcription_folder, "audio3_transcription.txt")
    with open(transcription_file_path, 'w', encoding='utf-8') as file:
        file.write(result["text"])
    print(f"Transcription saved to {transcription_file_path}")

if __name__ == '__main__':
    main()
