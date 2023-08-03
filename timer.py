import time
import threading
from playsound import playsound
from gtts import gTTS

inputs = []

inputs[0] = input("nechi soat: ")
inputs[1] = input("nechi minut: ")
inputs[2] = input("nechi sekund: ")

seconds = (inputs[0]*60*60)+(inputs[1]*60)+inputs[2]

mytext = "your timer is over, your timer is over, your timer is over, hey wake up, i said wake up, i am gonna kill your computer if you don't tur off this annoying alarm.                        wake up i said wake up, your timer is over"
audio = gTTS(text=mytext, lang="en", slow=False)
audio.save("example.mp3")


def playAlarm():
    playsound("./samsung_galaxy_alarm.mp3")
    return False


def playEx():
    playsound("example.mp3")
    return False


t1 = threading.Thread(target=playAlarm)

t2 = threading.Thread(target=playEx)


time.sleep(seconds)
print("timer completed")

t1.start()
t2.start()
