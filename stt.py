# This file contains the code relating to speech-to-text operations and functions
import speech_recognition as sr

recognizer = sr.Recognizer()

# Initial Prompt
with sr.Microphone() as source:
    print("911, do you need police, fire, or rescue?")
    audio = recognizer.listen(source)

# Interpret the initial request, and try to match the speech input to a specific department.
try:
    text = recognizer.recognize_google(audio)
    print(f"You said: {text}")
    
    if "fire" in text.lower():
        print("Fire Detected. Proceeding")
        # fire_func()
    elif "rescue" in text.lower():
        print("Rescue detected. Proceeding.")
        # rescue_func()
    elif "police" in text.lower():
        print("Police detected. Proceeding.")
        # police_func()
    else:
        print("No match of requested department found.")
    
except sr.UnknownValueError:
    print("Sorry, could not understand the audio")
except sr.RequestError:
    print("Could not request results; check your internet connection")
    
