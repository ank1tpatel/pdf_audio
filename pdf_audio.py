import os
from PyPDF2 import PdfReader
from gtts import gTTS
import time

def pdf_to_text(pdf_path):
    reader = PdfReader(pdf_path)
    text = ''
    for page_num, page in enumerate(reader.pages):
        text += page.extract_text()
    return text

def text_to_audio(text, audio_path):
    tts = gTTS(text)
    tts.save(audio_path)

def main():
    pdf_path = input("Enter the path to the PDF file: ").strip('"') # Remove double quotes around the file path

    # Start timing
    start_time = time.time()

    # Convert PDF to text
    text = pdf_to_text(pdf_path)

    # Generate text file path based on PDF file name
    text_filename = os.path.splitext(os.path.basename(pdf_path))[0] + '.txt'
    text_path = os.path.join(os.path.dirname(pdf_path), text_filename)

    # Save text to a file
    with open(text_path, 'w', encoding='utf-8') as file:
        file.write(text)

    # Generate audio file path based on PDF file name
    audio_filename = os.path.splitext(os.path.basename(pdf_path))[0] + '.mp3'
    audio_path = os.path.join(os.path.dirname(pdf_path), audio_filename)

    # Convert text to audio
    text_to_audio(text, audio_path)

    # End timing
    end_time = time.time()
    execution_time = end_time - start_time
    print(f"Script execution time: {execution_time:.2f} seconds")

    print('Conversion complete.')

if __name__ == '__main__':
    main()