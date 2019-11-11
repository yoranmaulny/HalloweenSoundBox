#!/usr/bin/python

# Importation des librairies pythons
from gpiozero import MotionSensor
from gpiozero import PWMLED
import random
import pygame

#GPIO utilise
GPIO_PIR = 4
GPIO_LED1 = 13
GPIO_LED2 = 19

pir = MotionSensor(GPIO_PIR)
ledG = PWMLED(GPIO_LED1)
ledD = PWMLED(GPIO_LED2)

ledG.value = 0
ledD.value = 0

pygame.init()

def playSound(_son, _repeat=0):
    pygame.mixer.init()
    pygame.mixer.music.load(_son)
    pygame.mixer.music.play(loops=_repeat)


def waitSound():
    while pygame.mixer.music.get_busy() == True:
        continue

def playDefenestration():
    #Duree du son 1s
    print " Defenestration"
    ledG.pulse(0.5,0.5,2)
    ledD.pulse(0.5,0.5,2)
    playSound("/home/pi/son/defenestration.wav", 1)

def playFantome():
    #Duree du son 2s
    print " Fantome"
    ledG.pulse(0.5,0.5,2)
    ledD.pulse(0.5,0.5,2)
    playSound("/home/pi/son/fantome.wav")

def playSorciere():
    #Duree du son 3s
    print " Sorciere"
    ledG.pulse(0.5,0.5,3)
    ledD.pulse(0.5,0.5,3)
    playSound("/home/pi/son/sorciere.wav")

def playToctoc():
    #Duree du son 3s
    print " Toctoc"
    ledG.blink(on_time=0.5,off_time=0.5,n=6)
    ledD.blink(on_time=0.5,off_time=0.5,n=6)
    playSound("/home/pi/son/toctoc.wav", 1)

def playZombie():
    #Duree du son 6s
    print " Zombie"
    ledG.pulse(1,1,3)
    ledD.pulse(1,1,3)
    playSound("/home/pi/son/zombie.wav")

def playLoup():
    #Duree du son 6s
    print " Loup"
    ledG.pulse(3,3,2)
    ledD.pulse(3,3,2)
    playSound("/home/pi/son/loup.wav", 1)

def playRire():
    #Duree du son 3s
    print " Rire"
    ledG.blink(on_time=0.5,off_time=0.5,n=6)
    ledD.blink(on_time=0.5,off_time=0.5,n=6)
    playSound("/home/pi/son/rire.wav", 1)

while True :
    print " Attente mouvement"
    pir.wait_for_motion()
    
    print " Mouvement detecte"
    sequence = random.randint(0,6)

    if sequence == 0 :
        playDefenestration()
    elif sequence == 1 :
        playFantome()
    elif sequence == 2 :
        playSorciere()
    elif sequence == 3 :
        playToctoc()
    elif sequence == 4 :
        playZombie()
    elif sequence == 5 :
        playLoup()
    else :
        playRire()

    waitSound()

    ledG.value = random.randint(0, 1)
    ledD.value = random.randint(0, 1)

    print " Attente mouvement"
    pir.wait_for_no_motion()