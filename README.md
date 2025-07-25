# Jarvis AI - Voice Assistant with GUI

A Python-based desktop voice assistant with a Tkinter GUI that listens to your voice commands and performs tasks like searching Wikipedia, playing music, telling jokes, opening websites, and reporting time and date.

---

## 🧠 Features

- 🔊 Voice command recognition using SpeechRecognition
- 📚 Wikipedia search with smart query cleanup
- 🎵 Play music from your local device
- 😂 Tells programming jokes (using pyjokes)
- 🕐 Reports current time and date
- 🌐 Opens Google and YouTube in browser
- 🖥️ GUI interface built with Tkinter
- 🚫 Gracefully exits on "exit", "stop", or "quit"

---

## 📌 Technologies Used

- Python 3.x
- Tkinter (GUI)
- pyttsx3 (Text-to-speech)
- SpeechRecognition (Voice recognition)
- PyAudio (for microphone input)
- Wikipedia API
- PyJokes (for humor)
- Pygame (for music playback)

---

## 💻 Setup Instructions

1. Clone the repository

   git clone https://github.com/yourusername/jarvis-ai-voice-assistant.git
   cd jarvis-ai-voice-assistant

2. Install dependencies
   pip install pyttsx3 SpeechRecognition wikipedia pyjokes pygame
   pip install pipwin
   pipwin install pyaudio

3. Run the app
   python voice assistant.py

4.  Set Custom Music Path
   
   In the code, replace this path with the actual location of your .mp3 file:

   file_path = r"C:\Users\YOURNAME\Downloads\your-music-file.mp3"   
