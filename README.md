Speech-to-Text Converter

A Python-based desktop application that converts spoken words into written text using speech recognition.

The application captures voice input through a microphone, converts the speech into text using Google Speech Recognition, displays the recognized text in a graphical user interface, and automatically saves the text to an "output.txt" file.

Technologies Used

- Python
- Tkinter
- SpeechRecognition
- PyAudio
- Google Speech Recognition
- Threading

Features

- Converts speech into text
- Uses a microphone for voice input
- Supports multiple languages
- Displays recognized text in a scrollable text area
- Automatically saves recognized text to "output.txt"
- Start Listening button
- Stop Listening button
- Clear button
- Displays status and error messages

Supported Languages

- English
- Telugu
- Hindi
- Tamil
- Kannada
- Malayalam

How to Run

1. Install the required packages

pip install -r requirements.txt

2. Run the application

python speech-to-text.py

3. Use the application

1. Select the required language.
2. Click Start Listening.
3. Speak into the microphone.
4. The application converts the speech into text.
5. The recognized text is displayed in the application.
6. The text is automatically saved to "output.txt".
7. Click Stop Listening to stop speech recognition.
8. Click Clear to clear the displayed text.

Output

The spoken words are converted into text and displayed in the application's text area.

The recognized text is also automatically stored in:

output.txt

Example:

Hello, this is my speech to text project.
This application converts speech into written text.

Project Structure

Speech-to-Text/
│
├── speech-to-text.py
├── requirements.txt
├── output.txt
└── README.md

File Description

- "speech-to-text.py" – Main Python program containing the desktop application.
- "requirements.txt" – Contains the required Python packages.
- "output.txt" – Stores the recognized speech as text.
- "README.md" – Project documentation.

Requirements

- Python 3.x
- Working microphone
- Internet connection for Google Speech Recognition
- Required Python packages listed in "requirements.txt"

Project Type

Desktop Application

Limitations

- Internet connection is required for Google Speech Recognition.
- Speech recognition accuracy may depend on microphone quality and background noise.
- Recognized text is stored locally in a text file.
- This project does not use a database or web-based frontend/backend.

Future Enhancements

- Add more language options
- Add Save As functionality
- Add PDF export
- Add timestamps to transcriptions
- Improve the graphical user interface
- Add offline speech recognition

Author
[KODIGUDLA ASWITHA]]