"""
The code is provided by https://techyowls.io/blog/speech-recognition-python-guide/

It simulates real-time transcription by using two threads

"""

import speech_recognition as sr
import threading
import queue

class RealtimeTranscriber:
    def __init__(self):
        self.recognizer = sr.Recognizer()
        self.audio_queue = queue.Queue()
        self.running = False

    def listen(self):
        with sr.Microphone() as source:
            self.recognizer.adjust_for_ambient_noise(source)
            print("Listening...")

            while self.running:
                try:
                    audio = self.recognizer.listen(source, timeout=1, phrase_time_limit=5)
                    self.audio_queue.put(audio)
                except sr.WaitTimeoutError:
                    continue

    def transcribe(self):
        while self.running or not self.audio_queue.empty():
            try:
                audio = self.audio_queue.get(timeout=1)
                text = self.recognizer.recognize_google(audio)
                print(f">> {text}")
            except queue.Empty:
                continue
            except sr.UnknownValueError:
                pass
            except sr.RequestError as e:
                print(f"Error: {e}")

    def start(self):
        self.running = True

        listen_thread = threading.Thread(target=self.listen)
        transcribe_thread = threading.Thread(target=self.transcribe)

        listen_thread.start()
        transcribe_thread.start()

        return listen_thread, transcribe_thread

    def stop(self):
        self.running = False

# Usage
transcriber = RealtimeTranscriber()
threads = transcriber.start()

input("Press Enter to stop...")
transcriber.stop()

for t in threads:
    t.join()