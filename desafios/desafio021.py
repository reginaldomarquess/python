# Faça um programa em python que abra e reproduza o áudio de um arquivo MP3.
# from time import sleep
import pygame

'''pygame.mixer.init()
w = pygame.mixer.Sound(
    "C:\\Users\\Reginaldo\\Desktop\\Variados\\base sólida python\\desafios\\exe021.mp3")
w.play()
sleep(10)'''

pygame.init()
pygame.mixer.music.load("desafios/exe021.mp3")
pygame.mixer.music.play()
pygame.event.wait()
input("Pressione enter para terminar a música...")
