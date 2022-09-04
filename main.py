# Reference link: https://medium.com/analytics-vidhya/speech-synthesizer-using-python-b3f1c83a1fc8

import pyttsx3

synthesizer = pyttsx3.init()
voices = synthesizer.getProperty('voices')
# for voice in voices: 
#     print("Voice:") 
#     print("ID: %s" %voice.id) 
#     print("Name: %s" %voice.name) 
#     print("Age: %s" %voice.age) 
#     print("Gender: %s" %voice.gender) 
#     print("Languages Known: %s" %voice.languages)

def change_voice(num):
    num=int(num)
    synthesizer.setProperty('voice', voices[num].id) 
    synthesizer.setProperty('rate', 150)
    synthesizer.setProperty('volume', 0.7)
    return synthesizer

def speak(text):
    my_text = str(text)
    print("JARVIS: ",text)
    synthesizer.say(my_text) 
    synthesizer.runAndWait() 
    synthesizer.stop()

print(synthesizer.getProperty('volume'))
change_voice(0)
speak("Hi tejas")
change_voice(1)
speak("Hi tejas")
change_voice(2)
speak("Hi tejas")