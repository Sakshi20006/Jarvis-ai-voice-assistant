import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import pyjokes
import tkinter as tk
from tkinter import scrolledtext, messagebox
import threading
import re

from playsound import playsound  # Optional: only if you're using music playback

# ------------------ Voice Engine Setup ------------------
engine = pyttsx3.init()
engine.setProperty('rate', 150)

def speak(text):
    output_box.insert(tk.END, f"Jarvis: {text}\n")
    output_box.see(tk.END)
    engine.say(text)
    engine.runAndWait()

# ------------------ Wikipedia Search ------------------
def get_wikipedia_summary(query):
    try:
        # Clean up query
        query = re.sub(r"^(what is|who is|tell me about|define|describe)\s+", "", query, flags=re.IGNORECASE).strip()

        # Search for best match
        search_results = wikipedia.search(query)
        if not search_results:
            return "Sorry, I couldn't find anything relevant."

        best_title = search_results[0]
        summary = wikipedia.summary(best_title, sentences=2)
        return summary
    except wikipedia.DisambiguationError as e:
        return f"Too many matches. Maybe you meant: {e.options[0]}"
    except wikipedia.PageError:
        return "No Wikipedia page found for your query."
    except Exception:
        return "Something went wrong while searching Wikipedia."

# ------------------ Assistant Logic ------------------
def wishMe():
    hour = int(datetime.datetime.now().hour)
    if 0 <= hour < 12:
        speak("Good Morning!")
    elif 12 <= hour < 18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")
    speak("I am your voice assistant. How can I help you?")

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        input_box.insert(tk.END, "Listening...\n")
        input_box.see(tk.END)
        r.pause_threshold = 1
        r.energy_threshold = 300
        try:
            audio = r.listen(source, timeout=5, phrase_time_limit=8)
        except Exception:
            return "None"

    try:
        query = r.recognize_google(audio, language='en-IN')
        input_box.insert(tk.END, f"You said: {query}\n")
        input_box.see(tk.END)
    except Exception:
        input_box.insert(tk.END, "Could not understand. Please try again.\n")
        input_box.see(tk.END)
        return "None"
    return query.lower()

# ------------------ Command Processing ------------------
def processCommand():
    start_btn.config(state=tk.DISABLED)
    wishMe()

    while True:
        query = takeCommand()
        if query == "none":
            continue

        if 'exit' in query or 'quit' in query or 'stop' in query:
            speak("Goodbye! Have a nice day.")
            break

        elif 'wikipedia' in query or 'what is' in query or 'who is' in query or 'tell me about' in query:
            speak("Searching Wikipedia...")
            result = get_wikipedia_summary(query)
            speak("According to Wikipedia")
            speak(result)

        elif 'open youtube' in query:
            webbrowser.open("https://www.youtube.com")

        elif 'open google' in query:
            webbrowser.open("https://www.google.com")

        elif 'play music' in query:
            try:
                playsound(r"C:\Users\SAKSHI CHOUDHARY\Downloads\promo-music-showreel-trailer-demo-ads-background-intro-theme-270169.mp3") # adjust the path as needed
            except:
                speak("Unable to play the music. Please check the file path.")

        elif 'time' in query:
            time_str = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"The time is {time_str}")

        elif 'date' in query:
            date_str = datetime.datetime.now().strftime("%Y-%m-%d")
            speak(f"Today's date is {date_str}")

        elif 'joke' in query:
            joke = pyjokes.get_joke()
            speak(joke)

        else:
            speak("Sorry, I didn't understand. Can you please repeat?")

    start_btn.config(state=tk.NORMAL)

# ------------------ GUI Functions ------------------
def startAssistant():
    # Prevent multiple threads
    if start_btn['state'] == tk.DISABLED:
        return
    threading.Thread(target=processCommand, daemon=True).start()

def exitApp():
    if messagebox.askokcancel("Exit", "Do you really want to exit?"):
        root.destroy()

# ------------------ GUI Setup ------------------
root = tk.Tk()
root.title("Jarvis Voice Assistant")
root.geometry("700x500")
root.configure(bg="#1e1e1e")

title = tk.Label(root, text="Jarvis AI - Voice Assistant", font=("Arial", 20, "bold"), fg="cyan", bg="#1e1e1e")
title.pack(pady=10)

input_box = scrolledtext.ScrolledText(root, height=10, width=80, bg="#333", fg="white", font=("Arial", 10))
input_box.pack(pady=10)
input_box.insert(tk.END, "Input Box:\n")

output_box = scrolledtext.ScrolledText(root, height=10, width=80, bg="#222", fg="lightgreen", font=("Arial", 10))
output_box.pack(pady=10)
output_box.insert(tk.END, "Output Box:\n")

start_btn = tk.Button(root, text="Start Listening 🎙️", command=startAssistant, bg="green", fg="white", font=("Arial", 12, "bold"))
start_btn.pack(pady=10)

exit_btn = tk.Button(root, text="Exit ❌", command=exitApp, bg="red", fg="white", font=("Arial", 12, "bold"))
exit_btn.pack(pady=5)

root.mainloop()
