
import speech_recognition as sr
AUDIO_FILE=("sample_simran.wav")
#use audio file as source

r= sr.Recognizer() #initialise the recogniser

with sr.AudioFile(AUDIO_FILE) as source:
    audio=r.record(source)
#reads the audio file

try:
    print ("audio file contains " + r.recognize_google(audio))
except sr.UnknownValueError :
    print ("Google Speech Recognition could not understand audio")
except sr.RequestError :
    print ("couldn't get the results from google speech recognition")