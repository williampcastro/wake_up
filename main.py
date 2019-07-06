from time import localtime
from pygame import mixer
import time

H = input("Informe a hora:  ")

m = input("Informe o minuto:  ")

while True:
    if localtime().tm_hour == int(H) and localtime().tm_min == int(m):
        print("É HORA DO SHOW!!!!")
        mixer.init()
        mixer.music.load("hora-do-shooow-porra.mp3")
        mixer.music.play()
        time.sleep(4)
        mixer.music.stop()
        mixer.music.load("music_one.mp3")
        mixer.music.play()
        time.sleep(360)
        break