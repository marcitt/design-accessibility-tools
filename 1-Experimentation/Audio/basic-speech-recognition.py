"""
The code is provided by https://techyowls.io/blog/speech-recognition-python-guide/

It enables a quick setup process but only allows one phrase to be sampled.

"""

import speech_recognition as sr

# Initialize recognizer
recognizer = sr.Recognizer()

# Recognize from microphone
with sr.Microphone() as source:
    print("Adjusting for ambient noise...")
    recognizer.adjust_for_ambient_noise(source, duration=1)

    print("Speak now...")
    audio = recognizer.listen(source, timeout=5)

    try:
        # Using Google's free API
        text = recognizer.recognize_google(audio)
        print(f"You said: {text}")
    except sr.UnknownValueError:
        print("Could not understand audio")
    except sr.RequestError as e:
        print(f"API error: {e}")