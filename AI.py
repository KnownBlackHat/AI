from gtts import gTTS
import os
def talktome(audio):
    print(audio)
    tts = gTTS(text=audio, lang='en-in', slow=False)
    tts.save("audio.mp3")
    os.system('mpv audio.mp3')
def command ():
    command = input('Tejas: ')
while(1):
    if command=hi:
        print ('hello,Sir!')
