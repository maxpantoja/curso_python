import pygame
#Faça um programa em Python que abra e reproduza o áudio de um arquivo MP3
pygame.mixer.init()
pygame.init()
pygame.mixer.music.load('ex021.mp3')
pygame.mixer.music.play(loops=0, start=0.0)
pygame.event.wait()