# Python program to translate
# speech to text and text to speech


import speech_recognition as sr
import pyaudio

filename = "gettysburg.wav"

# Initialize the recognizer
r = sr.Recognizer()

# Loop

# open the file
with sr.AudioFile(filename) as source:
    # listen for the data (load audio to memory)
    audio_data = r.record(source)
    # recognize (convert from speech to text)
    text = r.recognize_google(audio_data)
    print(text)

f = open("output.txt", "a")
f.write(text)
f.close()