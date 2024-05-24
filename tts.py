import os
from gtts import gTTS
from pydub import AudioSegment
import math

def text_to_speech(text, language='ar', filename='output.mp3'):
    """
    Convert text to speech and save it as an MP3 file, showing progress.
    
    Parameters:
    - text: The text to convert to speech.
    - language: The language of the text (default is Arabic).
    - filename: The output MP3 filename.
    """
    try:
        # Split the text into smaller chunks
        chunk_size = 100  # Adjust chunk size as needed
        text_chunks = [text[i:i + chunk_size] for i in range(0, len(text), chunk_size)]
        
        # Initialize an empty audio segment
        combined_audio = AudioSegment.empty()
        
        total_chunks = len(text_chunks)
        
        for i, chunk in enumerate(text_chunks):
            tts = gTTS(text=chunk, lang=language, slow=False)
            chunk_filename = f"chunk_{i}.mp3"
            tts.save(chunk_filename)
            
            # Load the chunk and append it to the combined audio
            audio_chunk = AudioSegment.from_mp3(chunk_filename)
            combined_audio += audio_chunk
            
            # Delete the chunk file
            os.remove(chunk_filename)
            
            # Calculate and print progress
            progress = (i + 1) / total_chunks * 100
            print(f"Progress: {progress:.2f}%")
        
        # Export the combined audio as a single MP3 file
        combined_audio.export(filename, format="mp3")
        print(f"Saved MP3 file as {filename}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    # Define the file name of the input text file
    input_file = "input.txt"
    
    # Check if the input file exists
    if os.path.exists(input_file):
        # Read the content of the input file
        with open(input_file, 'r', encoding='utf-8') as file:
            arabic_text = file.read().strip()
        
        # Define the output file name
        output_file = "arabic_speech.mp3"
        
        # Convert text to speech and save it as an MP3 file
        text_to_speech(arabic_text, filename=output_file)
    else:
        print(f"Error: The file '{input_file}' does not exist.")
